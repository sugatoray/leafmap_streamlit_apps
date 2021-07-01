# Managing environment variables in VS Code

## **Environment variable definitions file**

source: https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file

Set: `"python.envFile": "${workspaceFolder}/.env"` in `.vscode/settings.json` file and define variables in the `.env` file.

## **Predefined variables**

source: https://code.visualstudio.com/docs/python/settings-reference#_predefined-variables

The Python extension settings support predefined variables. Similar to the general VS Code settings, variables use the ${variableName} syntax. Specifically, the extension supports the following variables:

- `${cwd}` - the task runner's current working directory on startup
- `${workspaceFolder}` - the path of the folder opened in VS Code
- `${workspaceRootFolderName}` - the name of the folder opened in VS Code without any slashes (`/`)
- `${workspaceFolderBasename}` - the name of the folder opened in VS Code without any slashes (`/`)
- `${file}` - the current opened file
- `${relativeFile}` - the current opened file relative to `workspaceFolder`
- `${relativeFileDirname}` - the current opened file's dirname relative to `workspaceFolder`
- `${fileBasename}` - the current opened file's basename
- `${fileBasenameNoExtension}` - the current opened file's basename with no file extension
- `${fileDirname}` - the current opened file's dirname
- `${fileExtname}` - the current opened file's extension
- `${lineNumber}` - the current selected line number in the active file
- `${selectedText}` - the current selected text in the active file
- `${execPath}` - the path to the running VS Code executable

For additional information about predefined variables and example usages, see the Variables reference in the general VS Code docs.
