// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
var output = '';
var isSidebarVisible = false;

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "textScan" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = vscode.commands.registerCommand('textScan.helloWorld', function () {
		// The code you place here will be executed every time your command is executed
		
		const editor = vscode.window.activeTextEditor;
		const editorPath = editor.document.uri.fsPath;
		const selection = editor.selection;
		let highlighted = "";
		if (selection && !selection.isEmpty) {
			const selectionRange = new vscode.Range(selection.start.line, selection.start.character, selection.end.line, selection.end.character);
			highlighted = editor.document.getText(selectionRange);
			// Display a message box to the user
		}
		else {
			vscode.window.showInformationMessage("None");
		}

		const path = require('path');
		console.log('File name:', __dirname);
		const pythonPath = __dirname + "\\prototype1.py"
		vscode.window.showInformationMessage(pythonPath);
		
		const spawner = require('child_process').spawn;
		const python_process = spawner('python', [pythonPath, editorPath, highlighted, output]);
		console.log('Input sent');

		python_process.stdout.on('data', (data) => {
			output += data.toString();
			console.log('Output of Python Program:\n', data.toString());
		});
	});

	context.subscriptions.push(disposable);

	const toggleDisposable = vscode.commands.registerCommand('textScan.toggleSidebar', function() {
		var panel;
		panel = vscode.window.createWebviewPanel('textScanOutput', 'Transcript', vscode.ViewColumn.Beside, {});
		panel.webview.html = `<pre>${output}</pre>`;
	});

	context.subscriptions.push(toggleDisposable);
	
}

// This method is called when your extension is deactivated
function deactivate() {}

module.exports = {
	activate,
	deactivate
}
