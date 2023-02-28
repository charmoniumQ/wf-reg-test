import dataclasses
import re
from typing import Optional, Any

from .engines import SnakemakePythonError, SnakemakeWorkflowError, SnakemakeRuleError, NextflowJavaError, NextflowSigterm, NextflowCommandError, NextflowMiscError, SnakemakeCondaError, NoSnakefileError, WorkflowTimeoutError
from .workflows import WorkflowError


@dataclasses.dataclass(frozen=True)
class HighLevelError:
    class_: str
    subclass: str = ""
    extra: Any = None


error_trunc = 500


def classify(error: Optional[WorkflowError]) -> HighLevelError:
    if isinstance(error, WorkflowTimeoutError):
        return HighLevelError("timeout")
    elif isinstance(error, NoSnakefileError):
        return HighLevelError("missing input", "snakefile")
    elif isinstance(error, SnakemakeWorkflowError):
        if error.kind == "MissingInputException":
            return HighLevelError("missing input")
        elif m := re.search("No such file or directory: '(.*)'", error.rest):
            return HighLevelError("missing input", m.group(1))
        elif m := re.search("MissingInputException: Missing input files for rule (.*):", error.rest):
            return HighLevelError("missing input", "rule " + m.group(1))
        elif error.kind == "SnakemakeError" and (m := re.search("Failed to pull singularity image from (.*):\n", error.rest, re.MULTILINE)):
            return HighLevelError("singularity", "singularity failed to pull image", m.group(1))
        else:
            return HighLevelError("unclassified", str(error)[:error_trunc])
    elif isinstance(error, SnakemakeRuleError):
        if error.kind == "MissingInputException":
            return HighLevelError("missing input", error.rule)
        else:
            return HighLevelError("unclassified", str(error)[:error_trunc])
    elif isinstance(error, SnakemakePythonError):
        if error.kind == "SystemExit" and "Snakefile" in error.rest:
            return HighLevelError("missing input")
        elif error.kind == "ModuleNotFound" and (m := re.search("No module named '(.*)'", error.rest)):
            return HighLevelError("missing dep", m.group(1))
        elif error.kind == "CalledProcessError" and "singularity" in error.rest:
            return HighLevelError("singularity")
        elif m := re.search("'(.*)' is a required property", error.rest):
            return HighLevelError("missing input", "property " + m.group(1))
        elif m := re.search("Please make sure that they are correctly defined before running Snakemake:\n(.*)", error.rest):
            return HighLevelError("missing input", "env " + m.group(1))
        elif "'biopython' needs to be installed" in error.rest:
            return HighLevelError("missing dep", "biopython")
        elif "but it is not present or accessible" in error.rest and (m := re.search(r"configfile (.*) but", error.rest)):
            return HighLevelError("missing input", "configfile " + m.group(1))
        elif "Rule is marked for between workflow caching but has multiple output files" in error.rest:
            return HighLevelError("workflow script error", "caching multiple outputs")
        elif error.kind == "WorkflowError" and "Function did not return" in error.rest:
            return HighLevelError("workflow script error")
        elif error.kind == "InputFunctionException":
            return HighLevelError("missing input")
        elif m := re.search("No such file or directory: '(.*)'", error.rest):
            return HighLevelError("missing input", m.group(1))
        else:
            # return HighLevelError("workflow step error")
            return HighLevelError("unclassified", str(error)[:error_trunc])
    elif isinstance(error, SnakemakeCondaError):
        return HighLevelError("conda", error.rest[:40])
    elif isinstance(error, NextflowSigterm):
        return HighLevelError("timeout")
    elif isinstance(error, NextflowCommandError):
        if "unexpected end of file" in error.error or "Unexpected EOF" in error.error:
            return HighLevelError("experiment error")
        elif m := re.search("(.*)\u2019: No such file or directory", error.error):
            return HighLevelError("workflow step error", m.group(1) + " not found")
        elif m := re.search("Could not run command: (.*) ", error.error):
            return HighLevelError("workflow step error", m.group(1))
        elif "ERROR: Please check samplesheet header" in error.output:
            return HighLevelError("missing input", "samplesheet")
        elif "Missing output file(s)" in error.process:
            return HighLevelError("workflow step error", "Missing output file(s)", error.error)
        elif m := re.search("Input file '(.*)' seems to be completely empty. Consider respecifying!", error.error):
            return HighLevelError("missing input", m.group(1))
        elif "argument of length 0\nExecution halted" in error.error:
            return HighLevelError("missing input", "", error.error)
        elif "FATAL: External invocation of comet.exe failed" in error.error:
            return HighLevelError("workflow step error", "comet.exe")
        elif "UNIQUE constraint" in error.error:
            return HighLevelError("workflow step error", "", error.error.split("\n")[-1])
        elif m := re.search("'(.*)' must be a? ?numeric", error.error):
            return HighLevelError("workflow step error", m.group(1))
        elif "Status: 400 Bad Request" in error.error:
            # return HighLevelError("network resource changed", error.process.split(" ")[0].split(":")[-1])
            return HighLevelError("network resource changed")
        elif m := re.search(r"Error: File not found \(the file '(.*)' could not be found\)", error.error):
            return HighLevelError("missing input", m.group(1))
        elif m := re.search("Failed to open the file (.*)", error.error):
            return HighLevelError("missing input", m.group(1))
        else:
            return HighLevelError("unclassified", str(error)[:error_trunc])
    elif isinstance(error, NextflowJavaError):
        if error.msg == "Unknown configuration profile: 'singularity'":
            return HighLevelError("missing input", "singularity profile")
        elif "Failed to pull singularity image" in error.msg:
            return HighLevelError("singularity", "failed to pull singularity image")
        elif error.kind == "java.lang.IllegalStateException" and error.msg.startswith("Include statement"):
            return HighLevelError("workflow script error", error.msg)
        elif error.kind.startswith("nextflow.dag"):
            return HighLevelError("workflow script error", error.kind)
        elif (m := re.search(r"\(([^()]+.groovy:[0-9]+)\)", error.rest)):
            return HighLevelError("workflow script error", error.kind, m.group(1))
        else:
            return HighLevelError("unclassified", str(error)[:error_trunc])
    elif isinstance(error, NextflowMiscError):
        if "BISMARK_SUMMARY" in error.rest:
            return HighLevelError("workflow script error", "input file name collision")
        elif error.class_ != "nextflow.processor.TaskProcessor":
            return HighLevelError("missing input", error.rest)
        else:
            return HighLevelError("unclassified", str(error)[:error_trunc])
    else:
      return HighLevelError("unclassified", str(error)[:error_trunc])
