# Logs
- 对模型进行了少量的修改
- MLP 和 ConvNet 都用过传递 config 参数构建
- MLP 和 ConvNet 都有 weight_share 和 auxiliary 两个参数, 最终模型应当是 weight_share 和 auxiliary 都为 True
- 重写 test.py, 新增 fit(), 用于 multi_round training
- 新增 model_select.py, 用于 模型筛选, 与 test.py 无关


# Experiment Design
## MLP
1. The architecture of MLP:
    - Different width and depth config for MLP
    - 不做任何特殊处理，只用ReLU， 不用dropout, 不用 weight sharing, 不用 auxiliary loss
    - 确定最优的结构

2. Apply different activation layer:
    - 在1中最优结构的基础上, 将ReLU 替换成不同的激活函数, 验证其对结果的影响
    - 确定最优的activation

3. Apply Dropout to MLP:
    - 在 1 和 2 最优结构的基础上, 使用dropout, 验证其对结果的影响
    - 确定最优的dropout rate

4. Apply weight sharing to MLP:
    - 在 1, 2, 3 最优结构的基础上, 使用weight sharing, 验证其对结果的影响
    - 期望: weight sharing 应该提升 accuracy

5. Apply auxiliary loss to MLP:
    - 在 1, 2, 3, 4 的基础上, 使用 auxiliary loss, 验证其对结果的影响
    - 使用 tradeoff, 确定最优的 tradeoff
    - 期望: auxiliary loss 应该能进一步提升 accuracy


## ConvNet
1. The architecture of ConvNet:
    - Different channel config for ConvNet
    - 不做任何特殊处理, 只用ReLU(最后的sigmoid除外), 不用 BatchNorm, 不用 weight sharing, 不用 auxiliary loss
    - 确定最优的结构

2. Apply different activation layer:
    - 在 1 中最优结构的基础上, 将 ReLU 替换成不同的激活函数, 验证其对结果的影响
    - 确定最优的activation

3. Apply BatchNorm to ConvNet:
    - 在 1 和 2 最优结构的基础上, 使用 BatchNorm, 验证其对结果的影响

4. Apply weight sharing to ConvNet:
    - 在 1, 2, 3 最优结构的基础上, 使用 weight sharing, 验证其对结果的影响
    - 期望: weight sharing 应该提升 accuracy

5. Apply auxiliary loss to ConvNet:
    - 在 1, 2, 3, 4 的基础上, 使用 auxiliary loss, 验证其对结果的影响
    - 使用 tradeoff, 确定最优的 tradeoff
    - 期望: auxiliary loss 应该能进一步提升 accuracy


## 代码结构
- 上述的 model selection 全部放在另外的文件中完成, 不需要写成一个通用的整体的代码, 只要详细记录每个结果, 助教不会无聊到花时间去跑我们 model selection 的
- 在 test.py 中, 使用最优结构 和 auxiliary loss


## Experiment Results
- 将实验结果按上述小点详细记录在下面

- MLP
1. The architecture of MLP：
 index              params       res
   420  [128, 64, 32, 256]  0.819000
   422  [128, 64, 32, 256]  0.816333
   281  [128, 16, 64, 256]  0.816000
   360  [128, 32, 128, 64]  0.816000
   282  [128, 16, 64, 256]  0.815667
   
 index              params     res
    42  [128, 64, 32, 256]  0.8106
    39  [128, 64, 16, 256]  0.8093
    28  [128, 16, 64, 256]  0.8089
    35  [128, 32, 64, 128]  0.8086
    40  [128, 64, 16, 512]  0.8083

2. Apply different activation layer:
- Choose the best arch: [128, 64, 32, 256]  0.819000
- ReLU:
    Accuracy mean: 0.8069000244140625, std: 0.0071561806835234165
- Tanh:
    Accuracy mean: 0.7776999473571777, std: 0.03965700790286064
- Sigmoid:
    Accuracy mean: 0.7570000290870667, std: 0.0050771781243383884
- SELU:
    Accuracy mean: 0.7620999217033386, std: 0.02994607202708721

3. Apply Dropout to MLP:
- According to results in 2, we stick to use ReLU activation for MLP
- p=0:
    Accuracy mean: 0.8069000244140625, std: 0.0071561806835234165
- p=0.2:
    Accuracy mean: 0.7980999946594238, std: 0.006279588211327791
- p=0.5:
    Accuracy mean: 0.8018000721931458, std: 0.006663333624601364
- p=0.8:
    Accuracy mean: 0.7129999399185181, std: 0.029257476329803467

4. Apply weight sharing to MLP:
- According to results in 3, we will not use dropout, i.e., dropout rate p=0
Accuracy mean: 0.8407999873161316, std: 0.006663334555923939

5. Apply auxiliary loss to MLP:
- According to result in 4, weight sharing will improve performance. Based on this, we add auxiliary loss
Accuracy mean: 0.8758999705314636, std: 0.006740425247699022 (NO Tradeoff)

Add tradeoff:[0.5000, 0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000,
        1.4000, 1.5000])
Accs:        [0.8758, 0.8784, 0.8817, 0.8794, 0.8840, 0.8795, 0.8756, 0.8807, 0.8821,
        0.8807, 0.8812]
std:         [0.003458, 0.007763, 0.004270, 0.007619, 0.004372, 0.006311, 0.005854, 0.008667, 0.005646, 0.008327, 0.011153]
Best tradeoff 0.9:
Accuracy mean: 0.8843000531196594, std: 0.004473372828215361


- ConvNet
1. The architecture of ConvNet:
 index                params   res
     8   [32, 64, 32, 512]  0.8262
     3  [16, 128, 64, 128]  0.8256
    16   [64, 32, 256, 32]  0.8232
    13   [32, 128, 64, 16]  0.8232
     9   [32, 64, 64, 256]  0.8229

2. Apply different activation layer:
- Choose the best arch: [32, 64, 32, 512]  0.8262
- ReLU:
    Accuracy mean: 0.8137999773025513, std: 0.02263626642525196
- Tanh:
    Accuracy mean: 0.7789000272750854, std: 0.05178041383624077
- Sigmoid:
    Accuracy mean: 0.5879999399185181, std: 0.06494782865047455
- SELU:
    Accuracy mean: 0.7812999486923218, std: 0.048108793795108795

3. Apply BatchNorm to ConvNet:
- According to results in 2, we stick to use ReLU activation for ConvNet
- w/ BN:
    Accuracy mean: 0.804599940776825, std: 0.04717155173420906
- w/o BN:
    Accuracy mean: 0.8137999773025513, std: 0.02263626642525196

4. Apply weight sharing to ConvNet:
- According to results in 3, we will not use Batch Norm for ConvNet
Accuracy mean: 0.8751999735832214, std: 0.008456417359411716

5. Apply auxiliary loss to ConvNet:
Accuracy mean: 0.9045000076293945, std: 0.005892553832381964

Add tradeoff: [0.5000,   0.6000,   0.7000,   0.8000,   0.9000,   1.0000,   1.1000,   1.2000,   1.3000,   1.4000,   1.5000]
Accs:         [0.9013,   0.9046,   0.9078,   0.9142,   0.9069,   0.9091,   0.9092,   0.9062,   0.9091,   0.9102,   0.9069]
std:          [0.008756, 0.011374, 0.005633, 0.007554, 0.008306, 0.003872, 0.008108, 0.006828, 0.007310, 0.004709, 0.008293]

Best tradeoff: 0.8
Accuracy mean: 0.9136000871658325, std: 0.0062751867808401585