## Running in Google Colab

1. Open `workshop.ipynb` in Google Colab from the GitHub repo.
2. Run the notebook setup cell near the top of the notebook. It runs `git clone`, switches into the cloned repo, and installs the dependencies.
3. Run the remaining cells one-by-one.

## Running Locally

### Setup

1. Install the [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

2. Run `uv sync`

3. Install the VS Code [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

4. Make a copy of the `.env.example` file, name it `.env` and fill in the missing values (ask another developer)

### Running the Workshop

1. Open a `.ipynb` file in a compatible editor like VS Code.

2. Run VS Code command `Notebook: Select Notebook Kernel` and select the kernel located at `.venv/bin/python`.

3. Run cells one-by-one to see results.
