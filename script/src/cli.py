from pick import pick
import util
import constants
from candy_machine import CandyMachine
import asyncio


async def main():
    title = 'Please choose what you want to do: '
    options = [
        'Create candy machine', 
        "Retry failed uploads",
        'Append or Overwrite  WL for existing collection',
        'Update public mint time',
        'Update presale mint time',
        'Update mint fee per mille',
        'Test mint']
    option, index = pick(options, title)
    if index == 0 :
        candy_machiner = CandyMachine(constants.MODE, constants.BATCH_NUMBER)
        await candy_machiner.create()
    elif index == 1:
        candy_machiner = CandyMachine(constants.MODE, constants.BATCH_NUMBER)
        await candy_machiner.retryFailedUploads()
    elif index == 2:
        util.append_or_overwrite_whitelist()
    elif index == 3:
        util.update_public_mint_time()
    elif index  == 4:
        util.update_presale_mint_time()
    elif index == 5:
        util.update_mint_fee()
    else:
        util.mint(num_mints = 1, amount_per_mint = 1)

        #  Used asyncio to run async function
if __name__ == "__main__":
    asyncio.run(main())