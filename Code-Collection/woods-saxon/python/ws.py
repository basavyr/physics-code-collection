import numpy as np

def Test_NP_MODULE():
    try:
        x=np.arange(0,10,1)
    except Exception as exc:
        print(f'Issues: {exc}')
    finally:
        print('All tests passed')

Test_NP_MODULE()