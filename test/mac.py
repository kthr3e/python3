import pulp
target_menu_list =["てりやき","ポテト","コーラ"]
#LpVariableで自由辺巣を作成。値は-∞から∞まで
#lowBoundで0から∞まで
#catで変数の種類指定
xs = [pulp.LpVariable('{}'.format(x), cat='Integer', lowBound=0) for x in target_menu_list]
print('{}'.format(x) for x in target_menu_list)
