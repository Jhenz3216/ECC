# Energy Coding Club 
As part of Oregon State University - Cascades's [Energy Coding Club](mailto:energycodingclub@gmail.com), this
repository will be used to practice github workflow and organize our community project.

## Software requirements
- Python version 3.5+ 64-bit

## Installing from Source
1. Using Git, navigate to a local target directory and clone repository:
    ```
    git clone https://github.com/kbrunik/ECC.git
    ```

2. Open a terminal and navigate to /ECC

3. Create a new virtual environment and change to it. Using Conda and naming it 'ecc':
    ```
    conda create --name ecc python=3.8 -y
    conda activate ecc
    ```

4. Install requirements:
    ```
    pip install -r requirements.txt
    ```

5. Verify setup by running an example:
    ```
    python examples/test.py
    ```


