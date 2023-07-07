# chroma_client_server
leaving this vague because i just work in linux/osx but install python3.8 however you can. im omitting the virtual env step, but go for it :)

- `pip install --upgrade pip`

- `git clone https://github.com/areyoukillingm3/chroma_client_server.git`

- `cd chroma_client_server`

- `cd server`

- `git clone git clone https://github.com/chroma-core/chroma.git`

- `python3.8 -m pip install -r ./chroma/requirements.txt`

- `python3.8 -m pip install -r ./chroma/requirements_dev.txt`

- `python3.8 -m pip install chromadb`

- in one terminal run `./server/server.sh`

- in another run `python3.8 ./client/app.py`

- if the client shows a `test` collection the server is running.  go nuts from there
