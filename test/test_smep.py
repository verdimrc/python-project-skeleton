"""Tests SageMaker entrypoint scripts under different sourcedirs.

Demonstrate good vs bad practices, where the good practice ensures no conflicting
package name across all sourcedirs.

See: src/smepu0?/bad_modname.py for more details.
"""

import pytest


@pytest.fixture(autouse=True)
def smep01_bad_modname(root_dir, monkeypatch, helpers):
    """Emulate past smep01 test which imported smep01/bad_modname.py."""
    monkeypatch.syspath_prepend(root_dir / "src" / "smep01")
    helpers.import_from_file("bad_modname", root_dir / "src" / "smep01" / "bad_modname.py")


@pytest.mark.parametrize("name", ["smep01", "smep02"])
def test_good_train(root_dir, monkeypatch, helpers, smep01_bad_modname, name):
    monkeypatch.syspath_prepend(root_dir / "src" / name)
    train = helpers.import_from_file(f"{name}_train", root_dir / "src" / name / "train.py")
    print(train.good_main())
    assert train.good_main() == f"{name}: train"


@pytest.mark.parametrize("name", ["smep01", "smep02"])
def test_good_inference(root_dir, monkeypatch, helpers, smep01_bad_modname, name):
    monkeypatch.syspath_prepend(root_dir / "src" / name)
    inference = helpers.import_from_file(f"{name}_inference", root_dir / "src" / name / "inference.py")
    print(inference.good_model_fn())
    assert inference.good_model_fn() == f"{name}: inference"


@pytest.mark.parametrize("name", ["smep01", "smep02"])
def test_bad_train(root_dir, monkeypatch, helpers, smep01_bad_modname, name):
    """Demonstrate smepu02/train.py wrongly uses smepu01/bad_modname.py."""

    # Purposely show the ineffectiveness of sys.path monkey-patching.
    monkeypatch.syspath_prepend(root_dir / "src" / name)

    train = helpers.import_from_file(f"{name}_train", root_dir / "src" / name / "train.py")
    print(train.bad_main())
    assert train.bad_main() == f"{name} - SageMaker EntryPoint 01: train"


@pytest.mark.parametrize("name", ["smep01", "smep02"])
def test_bad_inference(root_dir, monkeypatch, helpers, smep01_bad_modname, name):
    """Demonstrate smepu02/inference.py wrongly uses smepu01/bad_modname.py."""

    # Purposely show the ineffectiveness of sys.path monkey-patching.
    monkeypatch.syspath_prepend(root_dir / "src" / name)

    inference = helpers.import_from_file(f"{name}_inference", root_dir / "src" / name / "inference.py")
    print(inference.bad_model_fn())
    assert inference.bad_model_fn() == f"{name} - SageMaker EntryPoint 01: inference"
