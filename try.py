import decryp
# クラスのインスタンスを作成
decryptor = decryp.decryp()

# 鍵とIVの設定
key_file_path = "assets/key/getKey"
iv_hex = "745ebf63a647a56f7e9bae165d9fce92"
decryptor.setkey_iv(key_file_path, iv_hex)

# 暗号化するファイルのパス
input_file_path = "/Users/sugiyamakota/Downloads/index2.ts"

# 復号化後のファイルの保存先
output_file_path = "/Users/sugiyamakota/Downloads/decript.ts"

# ファイルの復号化
decryptor.decrypt_file(input_file_path, output_file_path)

print("ファイルの復号化が完了しました。")


# # 使用例
# decrypt_file("assets/video/assets/m3u8/index389.ts",
#              "assets/key/getKey", "745ebf63a647a56f7e9bae165d9fce92")
