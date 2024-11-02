#type: ignore
FORMATS={'plank_time':5.39e-44,'yoctosecond':1e-24,'zeptosecond':1e-21,'attosecond':1e-18,'femtosecond':1e-15,'picosecond':1e-12,'nanosecond':1e-09,'microsecond':1e-06,'millisecond':.001,'second':1.,'minute':6e1,'hour':36e2,'day':864e2,'week':6048e2,'year':31536e3}
def convert_time(time,from_unit,to_unit):
 B=to_unit;A=from_unit
 if A not in FORMATS or B not in FORMATS:raise ValueError('Invalid unit specified')
 return time*(FORMATS[A]/FORMATS[B])
__all__=['convert_time']