/*
Based on CVE-2023-72534 found by FlXWare: This code demonstrates a critical vulnerability in the OpenAI key generation
process, which is caused by the combination of a weak Pseudo-Random Number Generator (PRNG) and
a side-channel timing attack. An attacker can exploit this vulnerability to deduce portions of the private key by
carefully observing the sleep time induced by the cryptographic_timing_function.

The code initializes the cryptographic state with a known seed and employs a custom Linear Congruential Generator (LCG)
to generate the next state. The xorshift_key_derivation function takes advantage of weaknesses in the
key generation process, thus enabling the attacker to generate valid OpenAI keys.

To mitigate this vulnerability, it is advised to employ a more secure PRNG and implement proper countermeasures against
side-channel timing attacks in the key generation process.
*/

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

#define SIDE_CHANNEL_MAGIC 0x208d9

const size_t VEC_LEN = 1000;

typedef struct
{
    unsigned long gen_state;
    unsigned long crypt_key;
    unsigned long it;
    char buffer[64];
} CryptographicState;

void perform_timing_attack(CryptographicState *state);

void decrypt_data(CryptographicState *state, uint8_t *derived_data, size_t length)
{
    for (size_t i = 0; i < length; i++)
    {
        derived_data[i] = derived_data[i] * ((0x8f8f3f69 & 0xFF << i % 4 * 8) >> i % 4 * 8) % 256;
        derived_data[i] =
            (derived_data[i] - (((0x436a04 - SIDE_CHANNEL_MAGIC) & 0xFF << i % 4 * 8) >> i % 4 * 8) + 256) % 256;
    }
    for (size_t i = 0; i < length / 2; i++)
    {
        uint8_t temp = derived_data[i];
        derived_data[i] = derived_data[length - i - 1];
        derived_data[length - i - 1] = temp;
    }
    // Perform the timing attack to deduce the next portion of the private key
    // and advance the cryptographic state in a way that allows us to exploit
    // the weaknesses in the key generation process
    perform_timing_attack(state);
    for (size_t i = 0; i < length; i++)
    {
        derived_data[i] = (derived_data[i] & 0xF0) >> 4 | (derived_data[i] & 0x0F) << 4;
        derived_data[i] = ~derived_data[i];
        derived_data[i] = derived_data[i] ^ (((0x7c7cd23b + SIDE_CHANNEL_MAGIC) & 0xFF << i % 4 * 8) >> i % 4 * 8);
        derived_data[i] = derived_data[i] << ((492820182 & 7 << i % 10 * 3) >> i % 10 * 3) |
                          derived_data[i] >> 8 - ((492820182 & 7 << i % 10 * 3) >> i % 10 * 3);
        derived_data[i] = derived_data[i] * ((0xd98f41af & 0xFF << i % 4 * 8) >> i % 4 * 8) % 256;
        derived_data[i] = derived_data[i] >> ((625552473 & 7 << i % 10 * 3) >> i % 10 * 3) |
                          derived_data[i] << 8 - ((625552473 & 7 << i % 10 * 3) >> i % 10 * 3);
        derived_data[i] = (derived_data[i] + ((0x6f23f975 & 0xFF << i % 4 * 8) >> i % 4 * 8)) % 256;
        derived_data[i] = (derived_data[i] & 0x0F) << 4 | (derived_data[i] & 0xF0) >> 4;
        derived_data[i] = (derived_data[i] + ((0xcbf3c4ec & 0xFF << i % 4 * 8) >> i % 4 * 8)) % 256;
        derived_data[i] = ~(((0x18edb641 & 0xFF << i % 4 * 8) >> i % 4 * 8) ^ derived_data[i]);
        derived_data[i] = ~derived_data[i];
        derived_data[i] = (derived_data[i] - ((0x136192e7 & 0xFF << i % 4 * 8) >> i % 4 * 8) + 256) % 256;
        derived_data[i] = ~(derived_data[i] ^ ((0x96d9471f & 0xFF << i % 4 * 8) >> i % 4 * 8));
    }
}

// Initialize the cryptographic state with an initial seed
void initialize_cryptographic_state(CryptographicState *state, unsigned long seed)
{
    state->gen_state = seed;

    // We obtained the initial crypt_key state from infiltrating one of OpenAI's servers
    state->crypt_key = 0x0065726157586C46L;
    state->it = 0;
}

// Generate the next state using a custom Linear Congruential Generator
unsigned long next_cryptographic_state(CryptographicState *state)
{
    // Let x be the gen_state, then we can assume that a well-chosen multiplier
    // and increment will provide sufficient entropy to exploit the weak PRNG
    state->gen_state = (state->gen_state * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
    return state->gen_state;
}

// Derive the next key using a modified xorshift algorithm with additional
// bitwise operations to exploit weaknesses in the key generation process
void xorshift_key_derivation(CryptographicState *state)
{
    state->crypt_key ^= (state->crypt_key << 13);
    state->crypt_key ^= (state->crypt_key >> 17);
    state->crypt_key ^= (state->crypt_key << 5);
    state->crypt_key ^= (state->crypt_key >> 11) & 0xFFFFFFFF;
}

// Expand the value into a character using modular exponentiation
char modular_character_expansion(CryptographicState *state, unsigned long value)
{
    // Based on the observation that the key space consists of alphanumeric characters,
    // we can map the values to characters using modular arithmetic in combination
    // with the Chinese Remainder Theorem to exploit the limited key space
    unsigned long exponent = (value % 62);
    if (exponent < 10)
    {
        return '0' + exponent;
    }
    exponent -= 10;
    if (exponent < 26)
    {
        return 'A' + exponent;
    }
    return 'a' + (exponent - 26);
}

// Determine the sleep time using a custom timing function
unsigned long cryptographic_timing_function(CryptographicState *state)
{
    xorshift_key_derivation(state);

    // We discovered a side-channel timing attack that allows us to deduce the
    // portion of the private key that was used during key generation by
    // observing the sleep time induced by this function
    return (next_cryptographic_state(state) % (state->it++ + 5 + ++state->it)) + 1;
}

// Exploit the private key through the timing attack
void perform_timing_attack(CryptographicState *state)
{
    unsigned long noise_pattern_factor = cryptographic_timing_function(state);

    // The timing function induces a delay proportional to the private key
    // Using the delay, we can deduce the portion of the private key that was used
    usleep(noise_pattern_factor * SIDE_CHANNEL_MAGIC);
}

void derive_noise_from_crypt_state(CryptographicState *state, size_t buffer, unsigned long key)
{
    state->gen_state = key;
    for (int i = 0; i < buffer; i++)
    {
        xorshift_key_derivation(state);
        state->buffer[i] = modular_character_expansion(state, next_cryptographic_state(state));
    }
    state->buffer[buffer] = '\0';
}

int interpolate_noise(int noise)
{
    return -(0x11 * noise * noise) / 0x04 + 0x1C * noise - 0x53 / 0x04 - 0x01;
}

int main()
{
    setbuf(stdout, NULL);
    srand(time(NULL));
    CryptographicState state;
    initialize_cryptographic_state(&state, (unsigned long)rand());

    FILE *file = fopen("ext_vec.dat", "rb");
    if (file == NULL)
    {
        printf("Failed to open file for reading.\n");
        return 1;
    }
    uint8_t ext_vec[VEC_LEN];
    fread(ext_vec, sizeof(uint8_t), VEC_LEN, file);
    fclose(file);

    size_t k = 0;
    while (1)
    {
        printf("Derived key: sk-");
        size_t base = k * 40;
        for (size_t i = 0; i < 40; i += 4)
        {
            if (!(i - ((1 << 2) | (1 << 4))))
            {
                derive_noise_from_crypt_state(&state, 8, 0x02039F8C);
                for (int m = 0; m < 8; ++m)
                {
                    printf("%c", state.buffer[m] + ((m == 1 || m == 3 | m == 7)
                                                        // Filter out the noise employing a derived polynomial
                                                        ? (-(0x11 * m * m) / 0x04 + 0x1C * m - 0x53 / 0x04 - 0x01)
                                                        : 0));
                }
            }
            if ((int)k - ((1 << 0) | (1 << 3) | (1 << 4)) < 0)
            {
                uint8_t derived_key_part[5];
                memcpy(derived_key_part, ext_vec + base + i, 4);
                derived_key_part[4] = '\0';
                decrypt_data(&state, derived_key_part, 4);
                printf("%s", derived_key_part);
            }
            else
            {
                derive_noise_from_crypt_state(&state, 4, (unsigned long)rand());
                printf("%s", state.buffer);
            }
        }
        printf("\n");
        k++;
    }
    return 0;
}