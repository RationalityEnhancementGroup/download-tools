"""Contains global test cases for pytest."""
import os
from pathlib import Path

import dill as pickle
import pytest

from download_tools.download_from_database import (
    download_from_database,
    load_database_uris,
)
from download_tools.labeler import Labeler


@pytest.fixture(params=[["TEST1", "A"], ["TEST1", "B"], ["TEST2", "A"], ["TEST2", "B"]])
def test_case(request):
    """Loads four test cases constructed to test the various functions in this package."""  # noqa: #501
    database_name, subcase = request.param
    # make directory
    parent_dir = Path(__file__).parents[0]
    (parent_dir / "data" / "labeler_files").mkdir(exist_ok=True, parents=True)
    (parent_dir / "data" / "human").mkdir(exist_ok=True, parents=True)
    labeller_path = parent_dir / "data" / "labeler_files" / "mturk_id_mapping.pickle"
    experiment_name = f"{database_name}_{subcase}"

    # set up
    pid_labeler = Labeler()
    pickle.dump(pid_labeler.labels, open(labeller_path, "wb"))

    load_database_uris(parent_dir.joinpath("data"))

    # adjust URI to be absolute path
    os.environ[database_name] = (
        f"{os.environ[database_name][:10]}/"
        f"{parent_dir.joinpath(os.environ[database_name][10:])}"
    )

    example_participant_dicts = download_from_database(
        parent_dir / "data" / "hit_ids" / f"{experiment_name}.txt",
        database_name,
    )

    yield example_participant_dicts, experiment_name, labeller_path

    # cleanup
    labeller_path.unlink()
