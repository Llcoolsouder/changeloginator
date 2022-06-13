# BEHOLD! The Changelog-inator

Builds a changelog from the most recent tag to the current commit _or_ if no tags are present from the first commit on the current branch to the most recent commit.

The changeloginator expects commits to be in a certain format:

```text
<type>: <[optional] scope>: <description>
```

where type can be `fix`, `feature`, `breaking_change`, or `style`. _Only `fix` and `feature` tags are currently written to the output file._

## Installing Dependencies

This project builds with [poetry](https://python-poetry.org/). Installation instructions can be found on their website but for the sake of completeness, all you need to do is run:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Once that's set up, you can install all of the dependencies with `poetry install` from the project root.

## Development

To open VSCode with the poetry virtual environment, form the project root run:

```bash
poetry shell
code .
```

## Running Tests

To run the suite of unit tests (from the project root) do:

```bash
python3 -m unittest discover -b -s changeloginator/tests/
```

The `-b` flag is optional. It suppresses stdout on tests that pass.

## Build and Install

From the project root build with:

```bash
poetry build
```

and install with:

```bash
python3 -m pip install --user dist/*.whl
```

## Running

Now you can run the app anywhere, on any repo with:

```bash
python3 -m changeloginator <path to repo>
```

The usual `--help` and `-h` options are available as well.
