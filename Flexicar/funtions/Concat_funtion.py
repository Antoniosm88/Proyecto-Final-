def concat(*args):
        strs = [str(arg) for arg in args if not pd.isnull(arg)]
        return ','.join(strs) if strs else np.nan