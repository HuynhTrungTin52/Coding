def displacement(t0, t1):
	f=lambda t: 160 - 32*t
	F = lambda t: 160*t - 16*(t**2)
	return F(t1) - F(t0)


t_start = 0
t_end = 8
disp = displacement( t_start, t_end)
print(f"Displacement from t={t_start} to t={t_end}: {disp} ft")