# Generating Tree View of Project Structure

The project structure can be created as follows using `tree` command.

```sh
tree -a -I ".git" .
```

## Project Structure

### With Files...

```sh
# Command:
# tree -a -I ".git" .
.
├── apps
│   └── minimal_app
│       ├── app.py
│       ├── .artifacts
│       │   └── map.html
│       └── requirements.txt
├── docs
│   └── .gitkeep
├── .gitignore
├── .ipynb_checkpoints
├── my_map.png
├── project_structure.md
├── README.md
├── .secrets
│   ├── .env.secret
│   ├── .env.shared
│   └── readme.md
├── src
│   ├── app.py
│   ├── .gitkeep
│   ├── .ipynb_checkpoints
│   │   └── notebook-checkpoint.ipynb
│   └── notebook.ipynb
├── .streamlit
└── .vscode
    ├── INFO.md
    └── settings.json
```

### Without Files:

```sh
.
├── apps
│   └── minimal_app
│       └── .artifacts
├── docs
├── .ipynb_checkpoints
├── .secrets
├── src
│   └── .ipynb_checkpoints
├── .streamlit
└── .vscode
```
