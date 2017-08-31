def common_end(a, b):
  return len(a) > 0 and len(b) > 0 and a[0] == b[0] or a[len(a)-1] == b[len(b)-1]