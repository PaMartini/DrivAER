import setuptools

setuptools.setup(
    name="DrivAER",
    version="0.0.2",
    description="Identify driving transcriptional regulators in single cell embeddings",
    author='Lukas Simon, Fangfang Yan',
    author_email="lkmklsmn@gmail.com",
    packages=['DrivAER'],
    install_requires=['scikit-learn','scanpy','anndata', 'keras==2.3.1',
                      'pandas','seaborn','matplotlib','dca','tensorflow'
                      ],
    package_data={'DrivAER': ['data/*.txt','annotations/*.gmt','annotations/*.tsv']}
)
