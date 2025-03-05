


'''
###------Get fitted value------###

    model = smf.ols('Y~age+C(edu)+income', data = df).fit()
    y_pred = model.fittedvalues
'''
