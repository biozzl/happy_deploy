from playwright.sync_api import Playwright, sync_playwright, expect
import random
import time
wait_time = random.randint(20, 60)
sleep_time = random.randint(5, 10)
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(60000)
    page.goto("https://cloud.okteto.com/login")
    print("Connect to okteto.com") 
    time.sleep(10)
    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Log in with GitHub").click()
    time.sleep(10)  
    print("Log in with GitHub")   
    page1 = page1_info.value
    time.sleep(sleep_time)
    page1.get_by_label("Username or email address").click()
    page1.get_by_label("Username or email address").fill("${YONGHU}")
    time.sleep(sleep_time)
    page1.get_by_label("Password").click()
    page1.get_by_label("Password").fill("${PW}")
    time.sleep(sleep_time)
    page1.get_by_role("button", name="Sign in").click()
    time.sleep(10)
    page1.close()
    print("Log in okteto sucessful") 
    time.sleep(sleep_time)
    page.goto("https://cloud.okteto.com/")
    time.sleep(sleep_time)
    try:
      page.goto("https://cloud.okteto.com/spaces/${YONGHU}")
      time.sleep(sleep_time)
      page.locator(".ResourceListItemParentArrow > .Icon > svg").click()
      time.sleep(sleep_time)
      page.get_by_text("Deployment").click()
      print("oko Deployment")
    except Exception:
    # 在发生异常时执行的操作
        print("oko Deployment is err!")
        pass
    time.sleep(sleep_time)
    page.get_by_text("YAML").click()
    time.sleep(sleep_time)
    print("oko YAML")
    page.get_by_text("Logs").click()
    time.sleep(wait_time)
    print("oko Logs")
    page2 = context.new_page()
    page2.set_default_timeout(60000)
    try:
        page2.goto("https://webapp.io")
        print("goto webapp")
        time.sleep(sleep_time)
        page2.get_by_role("link", name="Login").click()
        time.sleep(sleep_time)
        print("Login webapp")
        page2.get_by_role("link", name="Log in with GitHub").click()
        time.sleep(2)
    except Exception:
    # 在发生异常时执行的操作
        print("goto webapp is err!")
        pass
    try:
         page2.get_by_label("Username or email address").click()
         time.sleep(2)
         print("Login email address")
         page2.get_by_label("Username or email address").fill("${YONGHU}")
         page2.get_by_label("Password").click()
         time.sleep(2)
         page2.get_by_label("Password").fill("${PW}")
         print("Login Password")
         page2.get_by_role("button", name="Sign in").click()
         time.sleep(sleep_time)
    except Exception:
    # 在发生异常时执行的操作
        print("Skip Log in with GitHub is err!")
        pass
    try:
         page2.get_by_role("link", name="Skip Onboarding").click()
        
    except Exception:
    # 在发生异常时执行的操作
        print("Skip Onboarding is err!")
        pass
    print("Logged in webapp successfully") 
    time.sleep(wait_time)  
    count = 0
    while count < 200:
      count += 1   
      print("第 {} 次保活开始".format(count))
      try:
        page2.bring_to_front()
        page2.goto("https://webapp.io/${YONGHU}/deployments")
        time.sleep(wait_time)
        print("goto webapp Deployments")
        element =   page2.get_by_text("onwebapp.io")
        element.click()
        print("goto yourname.onwebapp.io")
        time.sleep(wait_time)
        page2.get_by_role("button", name="Connect to debugging terminal").click()
        print("Connect to debugging terminal")
        time.sleep(sleep_time)
        page2.get_by_role("textbox", name="Terminal input").nth(4).press("Enter")
        time.sleep(sleep_time)
        page2.get_by_role("textbox", name="Terminal input").nth(4).fill(" ")
        page2.get_by_role("textbox", name="Terminal input").nth(4).press("Enter")
        time.sleep(wait_time)
        page2.get_by_role("button", name="Disconnect from debugging terminal").click()
        print("Disconnect from debugging terminal")
        time.sleep(wait_time)
      except Exception:
    # 在发生异常时执行的操作
        print("Swebapp 保活 is err!")
        pass
      try:
        page.bring_to_front()
        page.goto("https://cloud.okteto.com/spaces/${YONGHU}")
        time.sleep(wait_time)
        page.locator(".ResourceListItemParentArrow > .Icon > svg").click()
        time.sleep(wait_time)
        page.get_by_text("Deployment").click()
        print("oko Deployment")
        time.sleep(wait_time)
        page.get_by_text("YAML").click()
        time.sleep(wait_time)
        print("oko YAML")
        page.get_by_text("Logs").click()
        time.sleep(wait_time)
        print("oko Logs")
      except Exception:
    # 在发生异常时执行的操作
        print("kteto 保活 is err!")
        pass
      print("第 {} 次保活结束".format(count))
    page.bring_to_front()
    page.goto("https://cloud.okteto.com/spaces/${YONGHU}")
    time.sleep(wait_time)
    page.locator(".ResourceListItemParentArrow > .Icon > svg").click()
    time.sleep(wait_time)
    page.get_by_text("Deployment").click()
    print("oko Deployment")
    time.sleep(sleep_time)
    print("reten_to_oko")
    page.get_by_role("button", name="Restart").click()
    time.sleep(sleep_time)
    print("Restart oko") 
    time.sleep(sleep_time)
    print("Restarting...") 
    page.get_by_role("button", name="Restart Resource").click()
    time.sleep(sleep_time)
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
