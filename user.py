#EXTINF:-1 tvg-id="acesso🌩️" group-title="" tvg-name="Acesso" tvg-logo="https://tomatoanimes.com/_next/image?url=/images/happy-min.png&w=256&q=75",🌩️
http://2qq.pro/210213270/780923762
#######################
from metaflow import FlowSpec, step

class HelloNetflixFlow(FlowSpec):
    @step
    def start(self):
        print("Hello from Netflix Metaflow!")
        self.next(self.end)

    @step
    def end(self):
        print("Flow completed successfully!")

if __name__ == "__main__":
    HelloNetflixFlow()

from spectator import Registry
from flask import Flask

app = Flask(__name__)
registry = Registry()

@app.route('/')
def hello():
    registry.counter("endpoint.requests", {"path": "/"})().increment()
    return "OK"

if __name__ == "__main__":
    app.run()

# gateway.py
from fastapi import FastAPI, Request
import httpx

app = FastAPI()

# Rotas de proxy configuradas
ROUTES = {
    "/service1": "http://localhost:8001",
    "/service2": "http://localhost:8002"
}

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    # Determina destino com base em prefixo
    for prefix, target in ROUTES.items():
        if path.startswith(prefix.lstrip("/")):
            url = f"{target}/{path[len(prefix.lstrip('/')):]}"
            async with httpx.AsyncClient() as client:
                resp = await client.request(
                    request.method,
                    url,
                    headers=request.headers.raw,
                    content=await request.body()
                )
            return resp.text

    return {"error": "Rota não configurada"}

uvicorn gateway:app --reload --port 8080

import os, glob
from setuptools import setup, find_packages

with open("metaflow/version.py", mode="r") as f:
    version = f.read().splitlines()[0].split("=")[1].strip(" \"'")


def find_devtools_files():
    filepaths = []
    for path in glob.iglob("devtools/**/*", recursive=True):
        if os.path.isfile(path):
            filepaths.append(path)
    return filepaths


setup(
    include_package_data=True,
    name="metaflow",
    version=version,
    description="Metaflow: More AI and ML, Less Engineering",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Metaflow Developers",
    author_email="help@metaflow.org",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: Linux :: Linux X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    project_urls={
        "Source": "https://github.com/Netflix/metaflow",
        "Issues": "https://github.com/Netflix/metaflow/issues",
        "Documentation": "https://docs.metaflow.org",
    },
    packages=find_packages(exclude=["metaflow_test"]),
    py_modules=[
        "metaflow",
    ],
    package_data={
        "metaflow": [
            "tutorials/*/*",
            "plugins/env_escape/configurations/*/*",
            "py.typed",
            "**/*.pyi",
        ]
    },
    data_files=[("share/metaflow/devtools", find_devtools_files())],
    entry_points="""
        [console_scripts]
        metaflow=metaflow.cmd.main_cli:start
        metaflow-dev=metaflow.cmd.make_wrapper:main
      """,
    install_requires=["requests", "boto3"],
    extras_require={
        "stubs": ["metaflow-stubs==%s" % version],
    },
)

pip install fastapi uvicorn httpx

go get github.com/netflix/chaosmonkey/cmd/chaosmonkey

#EXTINF:-1 tvg-id="globosp" group-title="" tvg-name="GLOBO SP" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/1/1f/TV_Globo_logo_(April_2025).png",GLOBO SP
http://cd.cddclox.store:80/live/manoelpaimanu/981354922/275075.m3u8
