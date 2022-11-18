import pandas as pd
def dataToCsv(file, data, columns, target):
    data = list(data)
    columns = list(columns)
    file_data = pd.DataFrame(data, index=range(len(data)), columns=columns)
    file_target = pd.DataFrame(target, index=range(len(data)), columns=['target'])
    file_all = file_data.join(file_target, how='outer')
    file_all.to_csv(file_data) 

def savePoint(self,path,data):
    df= pd.DataFrame(data=data)
    df.to_csv(path)

if __name__ == "__main__":
    f = r"E:\\temp\\as\\test3.csv"
    list = [1,2,3,4,5,6,7]
    # fast = []
    # dic={}
    # dic["asNum"]=list
    # df= pd.DataFrame(data=dic)
    # df.to_csv(f)
    log = f"123\n\r"
    for L in list:
        with open(f,'a+') as file:
            file.write(L)
    
    print("打印完成")
