from pathlib import Path
import wf_reg_test.util
from wf_reg_test.workflows import FileBundle, File


def test_main() -> None:
    with wf_reg_test.util.create_temp_dir() as temp_dir:
        (temp_dir / "foo").write_text("hi")
        (temp_dir / "blah").mkdir()
        (temp_dir / "blah/foo").write_text("hello")
        (temp_dir / "bar").symlink_to("foo")
        (temp_dir / "baz").hardlink_to(temp_dir / "foo")
        expected = FileBundle(contents={
            Path('foo'): File(hash_algo='xxhash', hash_bits=64, hash_val=16899831174130972922, size=2, contents_url=None),
            Path('baz'): File(hash_algo='xxhash', hash_bits=64, hash_val=16899831174130972922, size=2, contents_url=None),
            Path('blah/foo'): File(hash_algo='xxhash', hash_bits=64, hash_val=2794345569481354659, size=5, contents_url=None),
        })
        assert FileBundle.create(temp_dir) == expected
