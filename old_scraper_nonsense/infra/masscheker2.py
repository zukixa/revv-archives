import random
import json
import aiohttp
import asyncio
import aiofiles


async def get_random_line_from_file(file_path):
    lines = []
    # async with aiofiles.open(file_path, mode="r") as file:
    #     async for line in file:
    #         lines.append(line.strip())
    if file_path == "valid_links.txt":
        lines = [
            "chat-gpt-next-web-1-yunfeijiaa.vercel.app",
            "chat-gpt-next-web-888.vercel.app",
            "chat-gpt-next-web-granken.vercel.app",
            "chat-gpt-next-web-kadaliao.vercel.app",
            "chat-gpt-next-web-leviyanx.vercel.app",
            "chat-gpt-next-web-muyeyong.vercel.app",
            "chat-gpt-next-web-navy-phi.vercel.app",
            "chat-gpt-next-web-prettybot.vercel.app",
            "chat-gpt-next-web-qinzhenlove.vercel.app",
            "chat-gpt-next-web-1-cyan.vercel.app",
            "chat-gpt-next-web-1-rev8.vercel.app",
            "chat-gpt-next-web-2-inky.vercel.app",
            "chat-gpt-next-web-ahca.vercel.app",
            "chat-gpt-next-web-alpha-five-51.vercel.app",
            "chat-gpt-next-web-alvin-up.vercel.app",
            "chat-gpt-next-web-axingde.vercel.app",
            "chat-gpt-next-web-beta-flame.vercel.app",
            "chat-gpt-next-web-bigbiggu.vercel.app",
            "chat-gpt-next-web-bolinc.vercel.app",
            "chat-gpt-next-web-bright2hu.vercel.app",
            "chat-gpt-next-web-cjpb.vercel.app",
            "chat-gpt-next-web-departever.vercel.app",
            "chat-gpt-next-web-duoyingkeji.vercel.app",
            "chat-gpt-next-web-eveyuyi.vercel.app",
            "chat-gpt-next-web-frankie-huang.vercel.app",
            "chat-gpt-next-web-fsry.vercel.app",
            "chat-gpt-next-web-guisense.vercel.app",
            "chat-gpt-next-web-hlei87.vercel.app",
            "chat-gpt-next-web-hteen.vercel.app",
            "chat-gpt-next-web-iota-six-71.vercel.app",
            "chat-gpt-next-web-kappa-neon.vercel.app",
            "chat-gpt-next-web-kpaxqin.vercel.app",
            "chat-gpt-next-web-lanshe.vercel.app",
            "chat-gpt-next-web-lex-1919.vercel.app",
            "chat-gpt-next-web-lgh1122.vercel.app",
            "chat-gpt-next-web-liuchuan95.vercel.app",
            "chat-gpt-next-web-mei-jing.vercel.app",
            "chat-gpt-next-web-oukan.vercel.app",
            "chat-gpt-next-web-ransekuang.vercel.app",
            "chat-gpt-next-web-tdhxnp.vercel.app",
            "chat-gpt-next-web-venenofsd.vercel.app",
            "chat-gpt-next-web-xinghu.vercel.app",
            "chat-gpt-next-web-yang-drab.vercel.app",
            "chat-gpt-next-web-zhbin1022.vercel.app",
            "chat-gpt-next-web-zhoubingyi.vercel.app",
            "chat-gpt-next-web-zytw.vercel.app",
            "chat-gpt-next-web-dfkj321.vercel.app",
            "chat-gpt-next-web-elizen.vercel.app",
            "chat-gpt-next-web-tongvivi.vercel.app",
            "chat-gpt-next-web-arcticlyc.vercel.app",
            "chat-gpt-next-web-bryantchan.vercel.app",
            "chat-gpt-next-web-casksteven.vercel.app",
            "chat-gpt-next-web-zulezhe.vercel.app",
            "chat-gpt-next-web-1-henna.vercel.app",
            "chat-gpt-next-web-43434045.vercel.app",
            "chat-gpt-next-web-eight-cyan.vercel.app",
            "chat-gpt-next-web-ttti.vercel.app",
            "chat-gpt-next-web-ychen-97.vercel.app",
            "chat-gpt-next-web-yifunxxx.vercel.app",
            "chat-gpt-next-web-astrickharren.vercel.app",
            "chat-gpt-next-web-blue-nu.vercel.app",
            "chat-gpt-next-web-ffr48.vercel.app",
            "chat-gpt-next-web-hamguy.vercel.app",
            "chat-gpt-next-web-iota-six-49.vercel.app",
            "chat-gpt-next-web-jarvismao.vercel.app",
            "chat-gpt-next-web-new-eight.vercel.app",
            "chat-gpt-next-web-rust-xi.vercel.app",
            "chat-gpt-next-web-woad-chi.vercel.app",
            "chat-gpt-next-web-wsyzsfxq.vercel.app",
            "chat-gpt-next-web-yongd.vercel.app",
            "chat-gpt-next-web-xixiangwu.vercel.app",
            "chat-gpt-next-web-five-indol.vercel.app",
            "chat-gpt-next-web-jueshancoder.vercel.app",
            "chat-gpt-next-web-keller0.vercel.app",
            "chat-gpt-next-web-span-t-s.vercel.app",
            "chat-gpt-next-web-yaoyao.vercel.app",
            "chat-gpt-next-web-1-topaz.vercel.app",
            "chat-gpt-next-web-bigbubu233.vercel.app",
            "chat-gpt-next-web-donotlb.vercel.app",
            "chat-gpt-next-web-edison.vercel.app",
            "chat-gpt-next-web-eta-eight-60.vercel.app",
            "chat-gpt-next-web-jerrybay.vercel.app",
            "chat-gpt-next-web-jerryliu369.vercel.app",
            "chat-gpt-next-web-jzlz.vercel.app",
            "chat-gpt-next-web-kumaboom.vercel.app",
            "chat-gpt-next-web-laipeng88.vercel.app",
            "chat-gpt-next-web-lake-omega-68.vercel.app",
            "chat-gpt-next-web-lileiaa.vercel.app",
            "chat-gpt-next-web-loadinghtml.vercel.app",
            "chat-gpt-next-web-nickypan.vercel.app",
            "chat-gpt-next-web-one-wine-67.vercel.app",
            "chat-gpt-next-web-pi-liard.vercel.app",
            "chat-gpt-next-web-qhat.vercel.app",
            "chat-gpt-next-web-qzh612.vercel.app",
            "chat-gpt-next-web-sinnyun.vercel.app",
            "chat-gpt-next-web-stormluke.vercel.app",
            "chat-gpt-next-web-suncxue.vercel.app",
            "chat-gpt-next-web-terry623.vercel.app",
            "chat-gpt-next-web-xiaokhkh.vercel.app",
            "chat-gpt-next-web-yejunqin.vercel.app",
            "chat-gpt-next-web-asdfunl.vercel.app",
            "chat-gpt-next-web-dyskyside.vercel.app",
            "chat-gpt-next-web-jiuhuo365.vercel.app",
            "chat-gpt-next-web-liwen-cn.vercel.app",
            "chat-gpt-next-web-ten-pi-35.vercel.app",
            "chat-gpt-next-web-tony-tang.vercel.app",
            "chat-gpt-next-web-whshang.vercel.app",
            "chat-gpt-next-web-zheng-jl.vercel.app",
            "chat-gpt-next-web-zwhstudy.vercel.app",
        ]
    elif file_path == "gpt-4.txt":
        lines = [
            "chatgpt-vercel-tawny-five.vercel.app",
            "chatgpt-vercel-trent112.vercel.app",
            "chatgpt-vercel-gold.vercel.app",
            "chatgpt-vercel-jungajang.vercel.app",
            "chatgpt-vercel-nu-ten.vercel.app",
            "chatgpt-vercel-one-lyart.vercel.app",
        ]
    else:
        lines = [
            "chatgpt-vercel-1-783548244-qqcom.vercel.app",
            "chatgpt-vercel-1-plum.vercel.app",
            "chatgpt-vercel-1-ruby.vercel.app",
            "chatgpt-vercel-amber.vercel.app",
            "chatgpt-vercel-amosink.vercel.app",
            "chatgpt-vercel-blond.vercel.app",
            "chatgpt-vercel-chudric.vercel.app",
            "chatgpt-vercel-clarkshao.vercel.app",
            "chatgpt-vercel-coral.vercel.app",
            "chatgpt-vercel-ebon.vercel.app",
            "chatgpt-vercel-eight-alpha.vercel.app",
            "chatgpt-vercel-feelapi.vercel.app",
            "chatgpt-vercel-five-tau.vercel.app",
            "chatgpt-vercel-i5tong.vercel.app",
            "chatgpt-vercel-ivory.vercel.app",
            "chatgpt-vercel-lfb-cd.vercel.app",
            "chatgpt-vercel-liart-five.vercel.app",
            "chatgpt-vercel-lime-six.vercel.app",
            "chatgpt-vercel-ljcute.vercel.app",
            "chatgpt-vercel-ludyii.vercel.app",
            "chatgpt-vercel-naddod.vercel.app",
            "chatgpt-vercel-one-blue.vercel.app",
            "chatgpt-vercel-one-omega.vercel.app",
            "chatgpt-vercel-panw98.vercel.app",
            "chatgpt-vercel-qumoptly.vercel.app",
            "chatgpt-vercel-rho-ruby.vercel.app",
            "chatgpt-vercel-sigma-lake.vercel.app",
            "chatgpt-vercel-sleavin.vercel.app",
            "chatgpt-vercel-sxk218.vercel.app",
            "chatgpt-vercel-tau-orpin.vercel.app",
            "chatgpt-vercel-tawny-five.vercel.app",
            "chatgpt-vercel-teal-eta.vercel.app",
            "chatgpt-vercel-ten-red.vercel.app",
            "chatgpt-vercel-ten-rho.vercel.app",
            "chatgpt-vercel-topaz-five.vercel.app",
            "chatgpt-vercel-two-psi.vercel.app",
            "chatgpt-vercel-woad-two.vercel.app",
            "chatgpt-vercel-xi-peach.vercel.app",
            "chatgpt-vercel-zuotiya.vercel.app",
            "chatgpt-vercel-1-ashy.vercel.app",
            "chatgpt-vercel-freya9933.vercel.app",
            "chatgpt-vercel-three-psi.vercel.app",
            "chatgpt-vercel-trent112.vercel.app",
            "chatgpt-vercel-1-mocha.vercel.app",
            "chatgpt-vercel-1072344372.vercel.app",
            "chatgpt-vercel-2023.vercel.app",
            "chatgpt-vercel-72vq.vercel.app",
            "chatgpt-vercel-alinz1986.vercel.app",
            "chatgpt-vercel-beiyaohhhc.vercel.app",
            "chatgpt-vercel-bice.vercel.app",
            "chatgpt-vercel-blue-nine.vercel.app",
            "chatgpt-vercel-blush-ten.vercel.app",
            "chatgpt-vercel-bobbanga.vercel.app",
            "chatgpt-vercel-cdata.vercel.app",
            "chatgpt-vercel-ceaserw.vercel.app",
            "chatgpt-vercel-ciao-7.vercel.app",
            "chatgpt-vercel-cirzear.vercel.app",
            "chatgpt-vercel-codertl.vercel.app",
            "chatgpt-vercel-codinget.vercel.app",
            "chatgpt-vercel-delta-topaz.vercel.app",
            "chatgpt-vercel-doutianye.vercel.app",
            "chatgpt-vercel-elliclee.vercel.app",
            "chatgpt-vercel-eta-umber.vercel.app",
            "chatgpt-vercel-gamma-inky.vercel.app",
            "chatgpt-vercel-glenwon.vercel.app",
            "chatgpt-vercel-godghost.vercel.app",
            "chatgpt-vercel-gold.vercel.app",
            "chatgpt-vercel-hazel-eta.vercel.app",
            "chatgpt-vercel-hazel-ten.vercel.app",
            "chatgpt-vercel-holdon-d.vercel.app",
            "chatgpt-vercel-hu2014.vercel.app",
            "chatgpt-vercel-inky-phi.vercel.app",
            "chatgpt-vercel-iota-indol.vercel.app",
            "chatgpt-vercel-jd-wang.vercel.app",
            "chatgpt-vercel-jet-kappa.vercel.app",
            "chatgpt-vercel-jet-three.vercel.app",
            "chatgpt-vercel-joexzy.vercel.app",
            "chatgpt-vercel-jungajang.vercel.app",
            "chatgpt-vercel-kaikl.vercel.app",
            "chatgpt-vercel-kappa-two.vercel.app",
            "chatgpt-vercel-kdf5000.vercel.app",
            "chatgpt-vercel-keanu.vercel.app",
            "chatgpt-vercel-kungsin.vercel.app",
            "chatgpt-vercel-lanaanl.vercel.app",
            "chatgpt-vercel-laolihai.vercel.app",
            "chatgpt-vercel-lazily.vercel.app",
            "chatgpt-vercel-leergo.vercel.app",
            "chatgpt-vercel-li0329.vercel.app",
            "chatgpt-vercel-llki.vercel.app",
            "chatgpt-vercel-lzyerste.vercel.app",
            "chatgpt-vercel-mirror.vercel.app",
            "chatgpt-vercel-mu-hazel.vercel.app",
            "chatgpt-vercel-murex-nine.vercel.app",
            "chatgpt-vercel-narwhrl.vercel.app",
            "chatgpt-vercel-neon-kappa.vercel.app",
            "chatgpt-vercel-nine-amber.vercel.app",
            "chatgpt-vercel-nine-tan.vercel.app",
            "chatgpt-vercel-nu-ten.vercel.app",
            "chatgpt-vercel-omega-six.vercel.app",
            "chatgpt-vercel-one-lyart.vercel.app",
            "chatgpt-vercel-pi-ebon.vercel.app",
            "chatgpt-vercel-pluslqm.vercel.app",
            "chatgpt-vercel-psi-lac.vercel.app",
            "chatgpt-vercel-psi-self.vercel.app",
            "chatgpt-vercel-qcd1234.vercel.app",
            "chatgpt-vercel-qipan2021.vercel.app",
            "chatgpt-vercel-red-ten.vercel.app",
            "chatgpt-vercel-redfiue.vercel.app",
            "chatgpt-vercel-rho-liart.vercel.app",
            "chatgpt-vercel-ruby-psi.vercel.app",
            "chatgpt-vercel-rust-psi.vercel.app",
            "chatgpt-vercel-sable-two.vercel.app",
            "chatgpt-vercel-sage-three.vercel.app",
            "chatgpt-vercel-sage-two.vercel.app",
            "chatgpt-vercel-sand.vercel.app",
            "chatgpt-vercel-self-pi.vercel.app",
            "chatgpt-vercel-seven-eta.vercel.app",
            "chatgpt-vercel-siddht1.vercel.app",
            "chatgpt-vercel-six-dun.vercel.app",
            "chatgpt-vercel-sooty-ten.vercel.app",
            "chatgpt-vercel-starium.vercel.app",
            "chatgpt-vercel-summer9957.vercel.app",
            "chatgpt-vercel-suxsu.vercel.app",
            "chatgpt-vercel-syy706.vercel.app",
            "chatgpt-vercel-taupe-iota.vercel.app",
            "chatgpt-vercel-taupe-xi.vercel.app",
            "chatgpt-vercel-ten-black.vercel.app",
            "chatgpt-vercel-ten-theta.vercel.app",
            "chatgpt-vercel-ten-wine.vercel.app",
            "chatgpt-vercel-test-iota.vercel.app",
            "chatgpt-vercel-three-vert.vercel.app",
            "chatgpt-vercel-tpinecone.vercel.app",
            "chatgpt-vercel-two-nu.vercel.app",
            "chatgpt-vercel-two-sandy.vercel.app",
            "chatgpt-vercel-umber.vercel.app",
            "chatgpt-vercel-vflash.vercel.app",
            "chatgpt-vercel-weixun12.vercel.app",
            "chatgpt-vercel-wine-tau.vercel.app",
            "chatgpt-vercel-x-steel.vercel.app",
            "chatgpt-vercel-xi-red.vercel.app",
            "chatgpt-vercel-xp9477.vercel.app",
            "chatgpt-vercel-xsfecho.vercel.app",
            "chatgpt-vercel-yeahtech.vercel.app",
            "chatgpt-vercel-yhb5678-sz.vercel.app",
            "chatgpt-vercel-yinanp.vercel.app",
            "chatgpt-vercel-yingxincui.vercel.app",
            "chatgpt-vercel-ykonly.vercel.app",
            "chatgpt-vercel-zeta-pink.vercel.app",
            "chatgpt-vercel-zj23564.vercel.app",
            "chatgpt-vercel-zwy1234.vercel.app",
            "chatgpt-vercel-abin-zh.vercel.app",
        ]
    return random.choice(lines)


async def send_request(url, headers, data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                f"https://{url}/api",
                headers=headers,
                json=data,
                raise_for_status=True,
            ) as resp:
                text = await resp.text()
                print(url)
                if (
                    not text
                    or text[0] == "{"
                    or "deactivated" in text
                    or "check your plan and billing details" in text
                ):
                    return None
                return text
        except Exception as e:
            print(f"Request error: {e}")
            return None


async def send_request2(url, headers, data):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                f"https://{url}/api/chat-stream",
                headers=headers,
                json=data,
                raise_for_status=True,
            ) as resp:
                text = await resp.text()
                if (
                    not text
                    or text[0] == "{"
                    or "deactivated" in text
                    or "check your plan and billing details" in text
                ):
                    return None
                return text
        except Exception as e:
            print(f"Request error: {e}")
            try:
                headers["Path"] = "/api/openai/v1/chat/completions"
                headers["Accept"] = "text/event-stream"
                async with session.post(
                    f"https://{url}/api/openai/v1/chat/completions",
                    headers=headers,
                    json=data,
                    raise_for_status=True,
                ) as resp:
                    content = ""
                    async for line in resp.content:
                        line = line.decode("utf-8").strip()
                        if not line or line.startswith(":"):
                            continue
                        json_data = json.loads(line[5:])
                        content += json_data["choices"][0]["delta"]["content"]

                    print("---------shitting my pants--------------")
                    print(content)
                    return content

            except Exception as e:
                print(f"Request error: {e}")
                return None
        return None


async def get_valid_response(file_path, prompt):
    resp_text = None
    while not resp_text:
        url = await get_random_line_from_file(file_path)
        if file_path == "valid_links2.txt":
            headers = {
                "authority": url,
                "method": "POST",
                "path": "/api",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "text/plain;charset=UTF-8",
                "origin": "https://" + url,
                "referer": "https://" + url + "/",
                "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            }

            data = {
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.6,
                "password": "",
                "model": "gpt-3.5-turbo",
            }
            resp_text = await send_request(url, headers, data)
        elif file_path == "gpt4.txt":
            headers = {
                "authority": url,
                "method": "POST",
                "path": "/api",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "text/plain;charset=UTF-8",
                "origin": "https://" + url,
                "referer": "https://" + url + "/",
                "sec-ch-ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            }

            data = {
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.6,
                "password": "",
                "model": "gpt-4",
            }
            resp_text = await send_request(url, headers, data)
        else:
            headers = {
                "Authority": url,
                "Method": "POST",
                "Path": "/api/chat-stream",
                "Scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9",
                "Content-Type": "application/json",
                "Origin": "https://" + url,
                "Path": "v1/chat/completions",
                "Referer": "https://" + url,
                "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            }

            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
                "stream": True,
            }
            resp_text = await send_request2(url, headers, data)
    return resp_text


# Sample usage as a standalone function call
# loop = asyncio.get_event_loop()
# output = loop.run_until_complete(get_valid_response("valid_links2.txt", "Hello world!"))
# print(output)
# n = 20  # Adjust this value as needed
# results = loop.run_until_complete(
#  asyncio.gather(
#       *[get_valid_response("valid_links2.txt", "Hello world!") for _ in range(n)]
# )
# )

# for i, result in enumerate(results):
#   print(f"Result {i}: {result}")
