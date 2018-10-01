
import binascii, hashlib, base58, argparse

def convert(z):
    # Step 1: get the privatekey in extended format, this is hexadecimal upper or lower case.
    private_key_static = z
    # Step 2: adding 38 in the front for select de MAINNET channel Rekel address
    extended_key = "38"+private_key_static
    # Step 3: first process SHA-256
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    # Step 4: second process SHA-256
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    # Step 5-6: add checksum info to end of extended key
    final_key = extended_key+second_sha256[:8]
    # Step 7: finally the Wallet Import Format (WIF) is generated in the format base 58 encode of final_key
    WIF = base58.b58encode(binascii.unhexlify(final_key))
    # Step 8: show the private key on usual format WIF for wallet import. Enjoy!
    print ("Private Key on WIF format below")
    print (WIF)
    print ("_________________________________")
    print ("Donations for BTC: 1PdT9edVvQNK4dpPu145rYu2jniap4sjC1")

parser = argparse.ArgumentParser()
parser.add_argument("num", help="Enter the privatekey extended in hexadecimal")
args = parser.parse_args()
convert(args.num)
#https://github.com/geniusprodigy/bitcoin-convertpvk
