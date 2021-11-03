df_fd["expts"] = df_fd["Team"].map(df_odds)
df_fd.expts = df_fd.expts.astype('float')
df_fd.Value = df_fd.Value.astype('float')
df_fd.FP = df_fd.FP.astype('float')
pts_bins = [.94, 1.0, 1.06]
val_bins = [.99, 1.0, 1.01]
df_fd["rkpts"] = pd.cut(df_fd.expts, 3, labels=pts_bins)
df_fd.rkpts = df_fd.rkpts.astype('float')
df_fd['vlpts'] = pd.cut(df_fd.Value, 3, labels=val_bins)
df_fd.vlpts = df_fd.vlpts.astype('float')
df_fd["new_expts"] = df_fd.FP * df_fd.vlpts * df_fd.rkpts
pd.set_option('display.max_rows', df_fd.shape[0]+1)
df_fd
