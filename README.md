# kibana-codelist-vis

A plugin for Kibana that translates field values into a text labels using code list

---

## Install

Releases of the plugin can be found at [https://github.com/TeskaLabs/kibana-codelist-vis/releases](https://github.com/TeskaLabs/kibana-codelist-vis/releases)

To install the plugin, copy url of a particular release's zip file and run the following command from the Kibana install path:

```
bin/kibana-plugin install [RELEASE_URL]
```

**Example**:

```
bin/kibana-plugin install https://github.com/TeskaLabs/kibana-codelist-vis/releases/download/v18.08.02k6.4.2/kibana_codelist_vis-18.08.02.zip
```

## Create a lookup


### Lookup index template

First create an index template for lookup documents in Elasticsearch.

```
curl --request PUT \
  --url 'http://localhost:9200/_template/x-lff-lookup' \
  --header 'Content-Type: application/json' \
  --data '{ 
  "index_patterns" : [".x-lff-lookup"],
  "mappings": {
    "lookup": {
      "properties": {
        "fieldType": {"type": "keyword"},
        "lookupType": {"type": "text"},
        "map": {
          "properties": {
            "key": {"type": "keyword"},
            "value": {"type": "text"}
          }
        }
      }
    }
  }
}
'
```

### Lookup

In this example we will create a lookup with the unique identifier `language`.

After you run the following command (assuming Elasticsearch is listening at `localhost:9200`) you will be able to configure format `Language` to Kibana fields of type `string` using the Kibana Management UI.

```
curl --request PUT \
  --url 'http://localhost:9200/.x-lff-lookup/lookup/x-lff-lookup:language' \
  --header 'Content-Type: application/json' \
  --data '{
  "lookupType": "Language",
  "fieldType": ["string"],
  "map": [
    {"key":"en", "value": "English"},
    {"key":"de", "value": "German"},
    {"key":"cs", "value": "Czech"}
  ]
}'
```

## Develop

This project has been built with npm package `generator-kibana-plugin` which is now deprecated. It assumes the following folder structure:

```
.
├── kibana
└── kibana-codelist-vis
```

### Prerequisites

- `nvm` - Node version manager (https://github.com/creationix/nvm)

```
nvm install v8.11.4
nvm use v8.11.4
```

- `yarn` - a Node package manager

```
npm install yarn
```

Prepare Kibana

```
$ git clone https://github.com/elastic/kibana.git
$ cd kibana
$ yarn install
$ yarn kbn bootstrap
```

Clone this repo

```
$ git clone https://github.com/TeskaLabs/kibana-codelist-vis.git
$ cd kibana-codelist-vis
$ yarn kbn bootstrap
```

### Run

Start kibana and have it include this plugin

```
yarn start --oss
```

### Build

Build release into folder `./build/`

```
yarn build
```

## Kibana Contributing Guide

See the [kibana contributing guide](https://github.com/elastic/kibana/blob/master/CONTRIBUTING.md) for instructions setting up your development environment. Once you have completed that, use the following yarn scripts.

  - `yarn kbn bootstrap`

    Install dependencies and crosslink Kibana and all projects/plugins.

    > ***IMPORTANT:*** Use this script instead of `yarn` to install dependencies when switching branches, and re-run it whenever your dependencies change.

  - `yarn start`

    Start kibana and have it include this plugin. You can pass any arguments that you would normally send to `bin/kibana`

      ```
      yarn start --elasticsearch.url http://localhost:9220
      ```

  - `yarn build`

    Build a distributable archive of your plugin.

  - `yarn test:browser`

    Run the browser tests in a real web browser.

  - `yarn test:server`

    Run the server tests using mocha.

For more information about any of these commands run `yarn ${task} --help`. For a full list of tasks checkout the `package.json` file, or run `yarn run`.
