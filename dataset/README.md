# Example Results

We use two ways to detect the line-arts: threshold (since the line-arts are always close to black) and Laplacian edge detection. Note that: global threshold methods do not work because of the local Hazy effect. So instead, we use Sauvola threshold, which is a local threshold method, to detect the edges.

<img src="https://github.com/wenshuo128/Automatic-Flat-Colouring/blob/master/dataset/try/1.jpg" width="200" alt="Original image"/>          <img src="https://github.com/wenshuo128/Automatic-Flat-Colouring/blob/master/dataset/try/Laplacian/1.png" width="200" alt="Laplacian edge detection"/>          <img src="https://github.com/wenshuo128/Automatic-Flat-Colouring/blob/master/dataset/try/threshold_sauvola%2021/1.png" width="200" alt="Sauvola threshold with window size = 21"/>          <img src="https://github.com/wenshuo128/Automatic-Flat-Colouring/blob/master/dataset/try/threshold_sauvola%207/1.png" width="200" alt="Sauvola threshold with window size = 7"/>


