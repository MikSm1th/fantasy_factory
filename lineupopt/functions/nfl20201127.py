
df_fd_def = df_fd.query("Position == 'D'")
df_fd = df_fd.query("Position != 'D'")
df_fd_def.head(3)

df_fd["expts"] = df_fd["Team"].map(df_odds)
df_fd.expts = df_fd.expts.astype('float')
df_fd.Value = df_fd.Value.astype('float')
df_fd.FP = df_fd.FP.astype('float')
pts_bins = [.95, 1.0, 1.05]
val_bins = [.95, 1.0, 1.05]
df_fd["rkpts"] = pd.cut(df_fd.expts, 3, labels=pts_bins)
df_fd.rkpts = df_fd.rkpts.astype('float')
df_fd['vlpts'] = pd.cut(df_fd.Value, 3, labels=val_bins)
df_fd.vlpts = df_fd.vlpts.astype('float')
df_fd["new_expts"] = df_fd.FP * df_fd.vlpts * df_fd.rkpts
df_fd

df_fd.FPPG = df_fd.new_expts
Y
#df_fd.query("Position == 'D'")
df_fd.head()

df_fd.Salary.unique()
