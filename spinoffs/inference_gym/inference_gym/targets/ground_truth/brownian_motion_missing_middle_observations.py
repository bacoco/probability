# Lint as: python2, python3
# Copyright 2020 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
r"""Ground truth values for `brownian_motion_missing_middle_observations`.

Automatically generated using the command:

```
python -m inference_gym.tools.get_ground_truth \
--target=brownian_motion_missing_middle_observations \
  --stan_samples=20000
```
"""

import numpy as np

IDENTITY_MEAN = np.array([
    0.05133242672914917,
    0.029862782610630533,
    -0.031172652529096907,
    -0.07075318960545621,
    -0.1583844461940377,
    -0.19261781848210915,
    -0.24623025585388952,
    -0.264733267168325,
    -0.2989393430659151,
    -0.2700758515983913,
    -0.31773207856893737,
    -0.36536468182198545,
    -0.4128638065738398,
    -0.4604214089786905,
    -0.5079741932406774,
    -0.55524427242247,
    -0.6023584168428662,
    -0.64943669886585,
    -0.6963831136912,
    -0.7433059037799999,
    -0.790619132115,
    -0.7983796528349999,
    -0.7891339084000001,
    -0.8025824564399999,
    -0.7752648389199999,
    -0.7473457639850001,
    -0.7393372513650001,
    -0.6700283629049999,
    -0.667771779875,
    -0.653251209085,
]).reshape((30,))

IDENTITY_MEAN_STANDARD_ERROR = np.array([
    0.00014181716314387078,
    0.0001719725929952751,
    0.000180664379864193,
    0.00018649969823781502,
    0.00019093563954681453,
    0.00019301426923023186,
    0.00019327148582606353,
    0.00019674440104255154,
    0.00021223021719243243,
    0.0002620973411063996,
    0.0003880705486572078,
    0.0004751036214596269,
    0.0005388635800449369,
    0.0005833985293383768,
    0.0006084870285888182,
    0.0006060860573592229,
    0.0005838143973624952,
    0.0005445030194543895,
    0.00047704658253454216,
    0.0003883601451455446,
    0.00026664231815590753,
    0.00021302623473493158,
    0.0001968879612195528,
    0.00019080238997937597,
    0.0001920684026262354,
    0.00019214338076227152,
    0.00019376190381442665,
    0.0001967889165926859,
    0.00020703553565995777,
    0.0002247900573871474,
]).reshape((30,))

IDENTITY_STANDARD_DEVIATION = np.array([
    0.07214992377320903,
    0.08127312545037664,
    0.08349001356226761,
    0.08414710603965538,
    0.0843151859802296,
    0.08430940724507661,
    0.08460519351230679,
    0.08584498371941957,
    0.08861350851375449,
    0.09955259105308314,
    0.13233196052115767,
    0.15330375867088028,
    0.1673401123971802,
    0.17632566290477852,
    0.1804658991216236,
    0.18041127744433721,
    0.1760917851200855,
    0.16744719487597098,
    0.15335398736934266,
    0.13224175417578204,
    0.09973729863526973,
    0.08874149660351235,
    0.08547810175070569,
    0.08451775349135425,
    0.0845633061867915,
    0.08454810894476136,
    0.08468750032343271,
    0.08589817870106213,
    0.09006645463203046,
    0.10377701114714358,
]).reshape((30,))