import pandas as pd 
import numpy as np 

class Data() : 
    def __init__(self) :
        self.data = pd.read_csv('data/train_data.csv')
        self.symptoms_df = pd.read_csv('data/Symptoms.csv')
        self.code_sym = [col for col in self.data.columns if col!='Diseases']
        self.descriptions = { col : list( self.symptoms_df[ self.symptoms_df['Code'] == col ]['Description'] )[0] \
                                    for col in self.code_sym }
        freq_counts = { col : self.data[col].sum() for col in self.code_sym}
        self.freq_counts = {k: v for k,v in sorted(freq_counts.items(), key= lambda item : -item[1]) }
        freq_counts_keys = list(self.freq_counts.keys())
        
        self.prev_options = np.random.choice(freq_counts_keys[:20],10, replace=False)
        self.prev_options_des = [self.descriptions[col] for col in self.prev_options]
        self.cur_options = [{'label':label , 'value':value } for label,value in zip(self.prev_options_des,self.prev_options) ]
        self.rem_options = [col for col in self.code_sym ]
        # self.selected_so_far = [] 
        self.fig = dict({
                        "data": [{"type": "bar",
                        "x": [],
                        "y": []}],
                        "layout": {"title": {"text": "Disease vs their probabilities"}}
                    })
        self.female_symp = ['fm_'+str(i) for i in range(6) ]

   
    def update_options(self, selected_options):
        new_options = []

        # case-1 : No option selected 
        if (len(selected_options) == 0 ):
            self.rem_options = [col for col in self.rem_options if col not in self.prev_options]
            new_options = self.rem_options[:6]
            new_options.extend(self.rem_options[-1:-5:-1])
            new_options = list(set(new_options))
            self.prev_options = new_options 

        # case - 2 : At least 1 options selected
        elif(len(selected_options)>0):
            self.rem_options = [col for col in self.rem_options if col not in self.prev_options]
            tmp_data = self.data[ self.data[ selected_options ].sum(axis=1)>0 ][ self.rem_options ]
            tmp_cols_sum = tmp_data.sum(axis=0)
            tmp_cols_sum = tmp_cols_sum[tmp_cols_sum>0]
            tmp_cols_sum= tmp_cols_sum.sort_values(ascending=False)
            new_options = list(tmp_cols_sum.index[:6])
            new_options.extend(list(tmp_cols_sum.index[-1:-5:-1]))
            new_options = list(set(new_options))
            self.prev_options = new_options 

            del tmp_data, tmp_cols_sum 

        
        self.prev_options_des = [self.descriptions[col] for col in self.prev_options ]
        self.cur_options = [{'label':label,'value':value} for label,value in zip(self.prev_options_des,self.prev_options)]

        del new_options

        return self.cur_options

dl = Data() 
print(dl.freq_counts)

