from mytool import DEBUG

if DEBUG:
    _stats = f'/mytool/myman/myman.py\n\t__name__: "{__name__}"\n\t__file__: "{__file__}"\n\t__package__: "{__package__}"'
    try:
        print(f'{_stats}\n\t__path__: "{__path__}"')
    except NameError:
        print(_stats)

import sys
from mytool import term


def h1(text):
    return term.color(text, 'bold', 'ul', 'sat white')


def h2(text):
    return term.color(text, 'ul', 'sat white')


def h3(text):
    return term.color(text, 'sat white')


def h4(text):
    return term.white(text)


def comment(text):
    return term.color(text, 'grey')


def ita(text, reset_normal=True):
    """
    `reset_normal` is `True` by default, which resets `normal` (everything).
    If `False`, only `italic` is reset.
    """
    return term.italic(text, reset_normal)


def usage():
    return f'''
myman {ita("<arg>", False)}
        node
        git
'''


def node():
    print(f"""{h1('node')}
    
      {h2('ES6 Modules with Typescript')}
        {h3('Node')}
          node v12^
          node --experimental-modules --es-module-specifier-resolution=node .
              {comment(f'{ita("--experimental-modules", False)} allows for {ita("import / export", False)} syntax.')}
              {comment(f'{ita("--es-module-specifier-resolution=node", False)} allows for %s (subdir. not name of module from {ita("package.json", False)})' % ita('import from "./giladbarnea"', False))}
                  {comment(ita('import from "./giladbarnea/index" is also possible'))}
              {comment(f'the dot is dependent on "main" field in root {ita("package.json", False)}')}
          import {{sayHi}} from "./giladbarnea";        {comment(f'watch the relative {ita("./")}')}
          {ita('"type": "module"')} in {ita("package.json")}

          {h4('Submodules')}
            Each subfolder's {ita("package.json")} has to have a {ita('"type": "module"')}
            Make sure {ita('modules')} and {ita('resolution')} flags are on

        {h3('Typescript')}
          {ita('"module": "es2015"')} in {ita("tsconfig.json")} (or later)
          {ita('"target"')} doesn't seem to matter
          {ita('"include"')} field has to have something
        
        {h3('Electron')}
          {h4('main.ts')}
            No {ita("export / import")}, only {ita("require")}
            {ita("webPreferences.experimentalFeatures")} and {ita("nodeIntegration")} don't seem to matter
          
          {h4('tsconfig.json')}
            "module": "es6"
            "outDir": "dist"
            "include": [ "src/**/*" ]
            "types": [ "./node_modules/electron" ]
            {comment('Not sure if needed:')}
            "lib": [ "es6", "dom" ]
            "baseUrl": "."     
            "paths": {{ "*" : [ "node_modules/*" ] }}
            "moduleResolution": "node"

          {h4('package.json')}
            "start": "electron ./dist/main.js"      {comment(f'(or {ita("electron .", False)} if "main" field directs to file)')}
            "dependencies": {{ "electron" : "7.1.0", "typescript" : "^3.7.0-beta" }}
            {comment('Not sure if needed:')}
            "type": "module"
          
          {h4('index.html')}
            {comment('Required for import/export:')}
            <script src="./dist/importfile.js" type="module"></script>
            <script src="./dist/exportfile.js" type="module"></script>
          
          {h4('renderer.ts')}
            if type="module" in index.html:
                use {ita("require")} and {ita("module.exports = ...")}
                to import: {ita('require("./dist/renderer.js")')}
            else: 
                vars / objs in this file are globally accessible    
          
          {h4('Debugging')}
            https://github.com/microsoft/vscode-recipes/tree/master/Electron
            In tsconfig.json compilerOptions, "inlineSourceMap": true, and in DevTools add root dir to workspace and restart.
                Optional: "inlineSources" : true (dependent on either inlineSourceMap or sourceMap) 

          {h4('Run with node')}
            node ./node_modules/.bin/electron .
      
      
      {h2('Typescript - general')}
        {h3('tsconfig.json')}
          
          {h4('"files"')}       
                                List of rel / abs file paths
                                Trumps "exclude" even if specified there
          {h4('"include"')}     
                                "files" specified => union of both.
                                "outDir" is excluded as long as "exclude" is not specified
                                Files in "include" can be filtered with "exclude".
          {h4('"exclude"')}     
                                When not specified, defaults to node_modules, bower_components, jspm_packages and <outDir>.
                                If B.ts is references by A.ts, B.ts can't be excluded unless A.ts is also excluded.
                                Compiler doesn't include possible outputs (eg index.d.ts / index.js).

          {h4('"types" / "typeRoots"')}
                                By default all **/node_modules/@types are included, also recursively.
                                A types package is a folder with a file called index.d.ts or a folder with a package.json that has a types field.
                                Folders under "types" must exist under ./node_modules/@types. Disables recursive inclusion. Example: "types" : ["node"]. 
                                "typeRoots" disables ./node_modules/@types. Good for local typing dirs. Example: "typeRoots" : ["./typings"]
          
          {h4('"module"')}
                                If specified "outFile", only "AMD" and "System" allowed. 
                                "ES6" and "ES2015" allowed only when "target" : "ES5" or lower.
          
          {h4('"paths"')}       
                                Map paths to {ita("baseUrl")}. (baseUrl: "." means where tsconfig.json is).
                                The mapped path is appended to {ita("baseUrl")} when it's a non-relative name. 
                                  This means {ita("folder1/file2")} => {ita("baseUrl/folder1/file2")}
                                Values in arrays are fallbacks; if file doesn't exist, move to next. 
                                Examples:
                                  "jquery" : ["node_modules/jquery/dist/jquery"]. This means importing "jquery" actually imports the long path.
                                  "*" : ["*"]   {ita("<moduleName> => <baseUrl>/<moduleName>")}
                                  "*" : ["generated/*"]   {ita("<moduleName> => <baseUrl>/generated/<moduleName>")}
                                
            
        
    """)


def git():
    print(f"""
      {h2('New repo from scratch')}
        cd {{...}}
        git init
        git add .
        
        {comment("Optional: after creating repo")}
        git remote add origin https://github.com/giladbarnea/bashscripts.git
        
        git push
      
      
      {h2('merge')}
        {h3('Force merge branches')}
          git push -f origin master
      
          {comment(f"keep content of {ita('better_branch', False)}, but record a merge")}
          git merge --strategy=ours master
          git checkout master
      
          {comment(f"fast-forward master up to the me")}
          git merge better_branch

      
      {h2('Branches')}
        {h3('Rename branch')}
          git branch -m new-name
          git push origin :old-name new-name
          git push origin -u new-name
      
        {h3(f"Revert to specific commit")}
          git reset --hard $SHA1
          git reset --soft HEAD@{{1}}
          git commit -m "Reverting to the state of the project at ..."
          git push
      
        {h3(f"Create new branch off of master")}
          git checkout -b newbranch master
          git push origin --set-upstream origin newbranch
        
        {h3(f"Force delete branch")}
          git branch -D branch_to_delete

        {h3(f"Clone branch")}
          git clone --branch somebranch https://github.com/tambien/Piano.git [dir]
      
      {h2('pull')}
        {h3('Pull specific file')}
          git checkout origin/somebranch -- path/to/file

        {h3('Pull specific patch')}
          git checkout -p origin/somebranch -- path/to/file
        
        {h3('Pull specific file from specific commit')}
          git checkout $SHA1 -- path/to/file
      
      {h2('commit')}
        {h3('commit specific file')}
          git commit path/to/file
      
      {h2('rebase')}
        {h3('Rebase branch-to-update onto (on top) branch-with-changes.')}
          {comment("This will apply changes from branch-with-changes to branch-to-update")}
          git checkout branch-to-update
          git rebase [-i] branch-with-changes
          
          {comment("In short:")}
          git checkout branch-to-update && git rebase branch-with-changes && git push
      
      {h2('diff')}
        git diff --compact-summary gilad    {comment("path/to/file (new) |  17 ++")}
        git diff --numstat gilad    {comment("17  0   path/to/file")}
        git diff --summary gilad    {comment("create mode 100644 path/to/file")}

        {h3('Lines of code')}
          git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904
          git ls-files | xargs wc -l
      
      {h2('rm')}
        {h3('Remove file only from online repo')}
          {comment(f"{ita('cached', False)} means only in online repo")}
          git rm --cached path/to/file && git commit -m "removed file from cache" && git push

      {h2('Compare')}
        {h3('Compare 2 commits / branches')}
          {comment(f"[..] line:line, [...] commit:commit")}
          https://github.com/Talship/sport-bingo/compare/gilad-staging...master

      {h2('prune')}
        {comment(f"update local copies of remote branches")}
        git fetch --prune origin
        
        {comment(f"remove info about removed remote branches")}
        git remote prune origin

      {h2('config')}
        {comment(f"ommit giladbarnea to get value")}
        git config --global user.name giladbarnea
        git config --global user.email giladbrn@gmail.com
        cd ~/ && printf '.idea\\n.vscode\\n.directory' > .gitignore_global
        git config --global core.excludesfile ~/.gitignore_global
        
        {comment(f"Set git to use the credential memory cache")}
        git config --global credential.helper cache

      {h2('reset')}
        {h3('uncommit file')}
          git reset --soft HEAD^    {comment('or HEAD~1 instead of HEAD^')}
          git reset HEAD {ita('path/to/unwanted_file')}
          {ita('# commit again now')}
    """)

def ssh():
    print(f"""{h1('ssh')}
    Check access to site
    ssh -T git@bitbucket.org
    
    Add ssh key
    eval `ssh-agent`
    ssh-add -K ~/.ssh/<private_key_file>
        
    Check if ssh valid:
    ssh-keygen -l -f /Users/gilad/.ssh/id_rsa.pub

    Create new ssh key:
    ssh-keygen
    """)
class MyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# locals().pop('__builtins__')
# pp(locals())
def main():
    ARGS_TO_FN = dict(node=node, git=git)
    try:
        arg = sys.argv[1]
    except IndexError:
        print(term.warn(f'myman.py no args. usage: {usage()}'))
        sys.exit(0)
    else:
        ARGS_TO_FN[arg]()
