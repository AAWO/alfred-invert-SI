# alfred-invert-SI
Calculate the inverse of a value with SI prefix

Example:
- from 50MHz (frequency) calculate 20ns (period)

## Usage

`inv <value> <SI prefix> [<unit>]`
   - `↩` - Copy the result to Clipboard

For example:
- `inv 60`     -> 16.667m
- `inv 20u`    -> 50k
- `inv 50 MHz` -> 20 nHz⁻¹

## Configuration

No configuration is needed.

## Used libraries

This workflow uses [QuantiPhy](https://github.com/KenKundert/quantiphy) Pyhon library. 
