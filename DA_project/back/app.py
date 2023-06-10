from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

df = pd.read_csv('data03.csv', encoding='cp949')

@app.route('/')
def main():
    labels = ["January", "February", "March", "April", "May", "June"]
    l = {
        'labels': labels,
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(255, 99, 132)",
                'borderColor': "rgb(255, 99, 132)",
                'data': [50, 5, 2, 7, 30, 20, 45],
            },
        ],
    }
    res = json.dumps(l)
    return res

@app.route('/test', methods=['POST', 'GET'])
def test():
    username = request.form['username']
    password = request.form['password']
    return jsonify({'username': username, 'password': password})

@app.route('/local_category_tochart')
def local_category_tochart():
    loc_list = '제주'
    category = "평균기온(°C)"
    temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
    d = {
        'labels': temp_df['일시'].values.tolist(),
        'datasets': [
            {
                'label': "My First dataset",
                'backgroundColor': "rgb(255, 99, 132)",
                'borderColor': "rgb(255, 99, 132)",
                'data': temp_df['평균기온(°C)'].values.tolist(),
            },
        ],
    }

    res = json.dumps(d)
    return res

@app.route('/local_category_list_tochart')
def local_category_list_tochart():
    loc_list = ['제주', '서울', '백령도', '부산', '울산', '대전']
    category = "평균기온(°C)"
    loc = []

    for i in range(len(loc_list)):
        loc.append(pd.DataFrame(df[df['지점명'] == loc_list[i]]))

    datasets = []

    for i in range(len(loc)):
        datasets.append({
                'label': loc_list[i],
                'backgroundColor': "rgb("+str(i*50)+", 99, 132)",
                'borderColor': "rgb(" + str(i*50) + ", 99, 132)",
                'data': loc[i][category].values.tolist(),
    })

    res = json.dumps({
        'labels': loc[0]['일시'].values.tolist(),
        'datasets': datasets,
    })
    return res

# @app.route('/local_category_tochart_1')
# def tlocal_category_tochart_1():
#     loc_list = '서울'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_2')
# def local_category_tochart_2():
#     loc_list = '백령도'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_3')
# def local_category_tochart_3():
#     loc_list = '부산'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_4')
# def local_category_tochart_4():
#     loc_list = '울산'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_5')
# def local_category_tochart_5():
#     loc_list = '울산'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_6')
# def local_category_tochart_6():
#     loc_list = '대전'
#     category = "평균기온(°C)"
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart__7')
# def local_category_tochart_7():
#     loc_list = '제주'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart__8')
# def local_category_tochart_8():
#     loc_list = '서울'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart__9')
# def local_category_tochart_9():
#     loc_list = '백령도'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_10')
# def local_category_tochart_10():
#     loc_list = '부산'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_11')
# def local_category_tochart_11():
#     loc_list = '울산'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_12')
# def local_category_tochart_12():
#     loc_list = '대전'
#     category = '최고기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최고기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_13')
# def local_category_tochart_13():
#     loc_list = '제주'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_14')
# def local_category_tochart_14():
#     loc_list = '서울'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_15')
# def local_category_tochart_15():
#     loc_list = '백령도'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_16')
# def local_category_tochart_16():
#     loc_list = '부산'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_17')
# def local_category_tochart_17():
#     loc_list = '울산'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_18')
# def local_category_tochart_18():
#     loc_list = '대전'
#     category = '최저기온(°C)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['최저기온(°C)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_19')
# def local_category_tochart_19():
#     loc_list = '제주'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_20')
# def local_category_tochart_20():
#     loc_list = '서울'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_21')
# def local_category_tochart_21():
#     loc_list = '백령도'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_22')
# def local_category_tochart_22():
#     loc_list = '부산'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_23')
# def local_category_tochart_23():
#     loc_list = '울산'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_24')
# def local_category_tochart_24():
#     loc_list = '대전'
#     category = '평균풍속(m/s)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균풍속(m/s)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res


# @app.route('/local_category_tochart_25')
# def local_category_tochart_25():
#     loc_list = '제주'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_26')
# def local_category_tochart_26():
#     loc_list = '서울'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_27')
# def local_category_tochart_27():
#     loc_list = '백령도'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_28')
# def local_category_tochart_28():
#     loc_list = '부산'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res

# @app.route('/local_category_tochart_29')
# def local_category_tochart_29():
#     loc_list = '울산'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res


# @app.route('/local_category_tochart_30')
# def local_category_tochart_30():
#     loc_list = '대전'
#     category = '평균운량(1/10)'
#     temp_df = pd.DataFrame(df[df['지점명'] == loc_list])
#     d = {
#         'labels': temp_df['일시'].values.tolist(),
#         'datasets': [
#             {
#                 'label': "My First dataset",
#                 'backgroundColor': "rgb(255, 99, 132)",
#                 'borderColor': "rgb(255, 99, 132)",
#                 'data': temp_df['평균운량(1/10)'].values.tolist(),
#             },
#         ],
#     }

#     res = json.dumps(d)
#     return res




if __name__ == '__main__':
    app.run()
