import os
for f in [f for f in os.listdir("C:/Users/aboyle/repos/alineo_analytics/Alineo_Analytics/qa/Analytics/Test_Files") if f.endswith('_data.dsd')]:
    print(os.path.basename(f).strip('data.dsd').strip('_'))
pass