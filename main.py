from webserver import app, webserver

if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    FRAME = pd.DataFrame(data=np.random.randn(3, 8), index=["A", "B", "C"])

    webserver.archive = FRAME
    app.run(port=7216, debug=True)
