# Kibana Plugins Library


## Setup development environment

### 1. Clone Kibana repo

Make sure you are in the same directory as this readme (should be `kibana/library/plugins`)

Replace `[VERSION_TAG]` with the version of Kibana for which you want to develop a plugin.

```
git clone --branch [VERSION_TAG] https://github.com/elastic/kibana.git
```

### 2. Switch to correct Node.js version

Install the Node Version Manager by following the readme on following URL

```
https://github.com/creationix/nvm/blob/master/README.md
```

You may want to load nvm into your PATH afterwards

```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm
```

**Find and install appropriate version of Node.js** with Node version manager. The needed version is saved to `kibana/.node-version`

```
REQ_NODE_VERSION=$(cat kibana/.node-version)
nvm install ${REQ_NODE_VERSION}
nvm use ${REQ_NODE_VERSION}
```


## Develop a new plugin


### 1. Install Node modules for Kibana

```
(cd kibana && npm install)
```

### 2. Generate plugin with a generator

```
npm install -g yo generator-kibana-plugin
```

In `kibana/library/plugins` create new plugin directory

```
mkdir my-new-plugin
```

Run the generator inside your plugin directory

```
cd my-new-plugin
yo kibana-plugin
```

### 3. Run Kibana with plugin loaded

Go to your **plugin directory**.

```
cd my-new-plugin
npm start
```

## Build an existing plugin

1. Make sure you're using **correct Node.js version** (see above)
2. Make sure plugin's node modules are installed

	```
	cd an-existing-plugin
	npm install
	```
3. Build the plugin

	```
	npm run build
	```
4. The plugin is built in `an-existing-plugin/build/an_exising_plugin-[VERSION].zip`
