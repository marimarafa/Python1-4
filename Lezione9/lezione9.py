def complex_statistical_function(x : float,distribution_type, **kwargs):
    if distribution_type == "geometric":
        p :float = kwargs["p"]
    elif distribution_type == "poisson":
        lambda_1 :float = kwargs["lambda_1"]
      



complex_statistical_function(x=1.0,distribution_type= "geometric", p= 5.0)
complex_statistical_function(x=2.0,distribution_type= "poisson", lambda_1= 5.0)