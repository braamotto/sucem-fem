import csv, os
import numpy as N

data_path = 'analytical'
data_path = os.path.join(os.path.dirname(__file__), data_path)
E_data_csv_files = ('E_vals_1_re.csv',
                    'E_vals_1_im.csv',
                    'E_vals_2_re.csv',
                    'E_vals_2_im.csv',
                    'test_pts_1.csv',
                    'test_pts_2.csv',)
E_data = {}
for df in E_data_csv_files:
    key = os.path.splitext(df)[0]
    filename = os.path.join(data_path, df)
    E_data[key] = N.array([[float(x) for x in l]
                       for l in csv.reader(file(filename))], N.float64)
    
problem_data = {}
for l in file(os.path.join(data_path, 'problem_data.txt')):
    k, v = l.split()
    v = float(v)
    problem_data[k]=v
    
E_1 = E_data['E_vals_1_re'] + 1j*E_data['E_vals_1_im']
E_2 = E_data['E_vals_2_re'] + 1j*E_data['E_vals_2_im']
r_1 = E_data['test_pts_1']
r_2 = E_data['test_pts_2']