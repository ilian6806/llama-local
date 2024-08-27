## Ollama
#### Ollama lib implementation for running local models. Includes gradio interface and API. This was made for openSUSE linux.

### Installation
```bash
# Clone the repository
git clone {repo_url}

# Install dependencies
cd ollama
python3.10 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Install ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the models you need
ollama pull {model_name}

# Start the server
sh ./gradio_start.sh

# Open the browser and go to {your_ip}:7860
```
### To use the API
```
sudo firewall-cmd --zone=public --add-port=11434/tcp --permanent
sudo firewall-cmd --reload

systemctl edit ollama.service
```
##### Add this lines to the top and close the editor:
```
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
Environment="OLLAMA_NUM_PARALLEL=4"
Environment="OLLAMA_ORIGINS=*"
```
##### Restart the service
```
systemctl daemon-reload
service ollama restart
```
##### You also have to fix SSL certificate if you want to use HTTPS

### Model preloading
By default, the models are loaded on demand. You can preload the model to avoid the delay when running it for the first time.

Preload the model:
```
sh ./model_preload.sh llama3.1:70b
```
Unload the model:
```
sh ./model_unload.sh llama3.1:70b
```

### Ollama lib usage
```
Usage:
  ollama [flags]
  ollama [command]

Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
```
### Screens usage

#### Usable commands
```
screen -S llama3           - create and attach
screen -S llama3 -X quit   - kill
screen -r llama3           - attach
screen -r                  - list or join if one
screen -ls                 - list
```

#### Inside screen
```
ctrl D             - kill
ctrl AD            - detach
```