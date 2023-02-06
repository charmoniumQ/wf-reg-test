- Use RDF
- Each triple is a claim about the world
- Each triple has provenance link
- Triples trivially support adding/subtracting data fields
- Each data release claims that these triples are exhaustive
- Map triples to Python dataclass
- Each data release has a set of Python dataclass that can interpret the triples

- Example: <https://github.com/common-workflow-language/cwlprov/blob/main/examples/revsort-run-1/metadata/provenance/primary.cwlprov.ttl>
- More deets: <https://github.com/common-workflow-language/cwlprov/blob/main/prov.md>

- Execution:
someone a prov:Agent;
    foaf:name blah;
    foaf:mbox blah;
    github-name blah.
something a prov:SoftwareAgent;
    prov:actedOnBehalfOf someone.
bundle a wfprov:Artifact, prov:Entity;
    prov:qualifiedGeneration [
        a prov:Generation
        prov:atTime time
    ].
workflow a wfdesc:Workflow.

- Relevant classes and properties:
  - doap:Project
    - doap:name
    - doap:homepage
    - doap:description
    - doap:license
    - doap:developer
      - foaf:Person
       - foaf:mbox
    - doap:programming-language
    - doap:release
      - doap:Version
        - doap:revision
    - doap:repository
      - doap:GitRepository
  - wfdesc:Workflow
    - wfdesc:hasSubProcess
      - wfdesc:Process
  - prov:Plan
  - prov:Agent
    - foaf:name
    - prov:SoftwareAgent
    - prov:actedOnBehalfOf
      - prov:Agent
  - https://oscaf.sourceforge.net/nfo.html
- Turn GitHub data into RDF:
  - http://www.semangit.de/

- https://github.com/Sage-Bionetworks-Workflows/nf-prov
- https://github.com/edgano/researchObject-Nextflow
- https://openprovenance.org/store/
- https://pypi.org/project/gitlab2prov/
