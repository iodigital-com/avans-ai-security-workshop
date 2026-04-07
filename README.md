## Setup

1. Install the [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

2. Run `uv sync`

3. Install the VS Code [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

4. Make a copy of the `.env.example` file, name it `.env` and fill in the missing values (ask another developer)

## Development

1. Open a `.ipynb` file in a compatible editor like VS Code.

2. Run VS Code command `Notebook: Select Notebook Kernel` and select the kernel located at `./analysis/.venv/bin/python`.

3. Run all cells to see all results, or selectively run the cells you want.
