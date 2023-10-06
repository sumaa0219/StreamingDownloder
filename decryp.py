from Crypto.Cipher import AES


class decryp():
    def setkey_iv(self, key_file_path, iv):
        self.key_hex = ""
        with open(key_file_path, "rb") as f:
            buf = f.read()
        for x in buf:
            self.key_hex += "{0:02x}".format(x)
        self.iv_hex = iv

    def decrypt_file(self, input_file, output_file):
        key = bytes.fromhex(self.key_hex)
        iv = bytes.fromhex(self.iv_hex)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        with open(input_file, 'rb') as infile:
            with open(output_file, 'wb') as outfile:
                while True:
                    chunk = infile.read(16)  # 16バイトずつ読み込む（AESブロックサイズ）
                    if not chunk:
                        break
                    decrypted_chunk = cipher.decrypt(chunk)
                    outfile.write(decrypted_chunk)
