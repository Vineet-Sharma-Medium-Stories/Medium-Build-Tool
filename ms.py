#!/usr/bin/env python3
"""
Medium Post Statistics Fetcher
Automatically loads cookies from browser and fetches current month stats
"""

import requests
import json
import sys
import sqlite3
import os
from datetime import datetime, timedelta
from pathlib import Path
import tempfile
import shutil

def get_chrome_cookies_linux():
    """Extract Medium cookies from Chrome on Linux"""
    cookie_paths = [
        Path.home() / ".config/google-chrome/Default/Cookies",
        Path.home() / ".config/google-chrome/Profile 1/Cookies",
        Path.home() / ".config/google-chrome/Profile 2/Cookies",
        Path.home() / ".config/chromium/Default/Cookies",
    ]
    
    for cookie_path in cookie_paths:
        if cookie_path.exists():
            try:
                # Copy the database because it might be locked
                temp_db = tempfile.NamedTemporaryFile(delete=False)
                temp_db.close()
                shutil.copy2(cookie_path, temp_db.name)
                
                conn = sqlite3.connect(temp_db.name)
                cursor = conn.cursor()
                
                # Query Medium cookies
                cursor.execute(
                    "SELECT name, value FROM cookies WHERE host_key LIKE '%medium.com%'"
                )
                
                cookies = {name: value for name, value in cursor.fetchall()}
                conn.close()
                
                # Clean up temp file
                os.unlink(temp_db.name)
                
                if cookies:
                    print(f"✅ Found {len(cookies)} cookies from Chrome")
                    return cookies
            except Exception as e:
                print(f"⚠️  Could not read cookies from {cookie_path}: {e}")
                continue
    
    return None

def get_chrome_cookies_mac():
    """Extract Medium cookies from Chrome on macOS"""
    cookie_path = Path.home() / "Library/Application Support/Google/Chrome/Default/Cookies"
    
    if cookie_path.exists():
        try:
            temp_db = tempfile.NamedTemporaryFile(delete=False)
            temp_db.close()
            shutil.copy2(cookie_path, temp_db.name)
            
            conn = sqlite3.connect(temp_db.name)
            cursor = conn.cursor()
            
            cursor.execute(
                "SELECT name, value FROM cookies WHERE host_key LIKE '%medium.com%'"
            )
            
            cookies = {name: value for name, value in cursor.fetchall()}
            conn.close()
            
            os.unlink(temp_db.name)
            
            if cookies:
                print(f"✅ Found {len(cookies)} cookies from Chrome")
                return cookies
        except Exception as e:
            print(f"⚠️  Could not read cookies: {e}")
    
    return None

def get_firefox_cookies():
    """Extract Medium cookies from Firefox"""
    firefox_profiles = list(Path.home().glob(".mozilla/firefox/*.default*"))
    
    for profile in firefox_profiles:
        cookie_path = profile / "cookies.sqlite"
        if cookie_path.exists():
            try:
                temp_db = tempfile.NamedTemporaryFile(delete=False)
                temp_db.close()
                shutil.copy2(cookie_path, temp_db.name)
                
                conn = sqlite3.connect(temp_db.name)
                cursor = conn.cursor()
                
                cursor.execute(
                    "SELECT name, value FROM moz_cookies WHERE host LIKE '%medium.com%'"
                )
                
                cookies = {name: value for name, value in cursor.fetchall()}
                conn.close()
                
                os.unlink(temp_db.name)
                
                if cookies:
                    print(f"✅ Found {len(cookies)} cookies from Firefox")
                    return cookies
            except Exception as e:
                print(f"⚠️  Could not read Firefox cookies: {e}")
                continue
    
    return None

def get_cookies_from_browser():
    """Try to get cookies from all supported browsers"""
    print("\n🔍 Attempting to load cookies from browser...")
    
    import platform
    system = platform.system()
    
    if system == "Linux":
        cookies = get_chrome_cookies_linux()
        if not cookies:
            cookies = get_firefox_cookies()
    elif system == "Darwin":  # macOS
        cookies = get_chrome_cookies_mac()
        if not cookies:
            cookies = get_firefox_cookies()
    elif system == "Windows":
        print("⚠️  Windows automatic cookie extraction not implemented yet")
        print("Please use manual cookie entry or export cookies from browser")
        return None
    else:
        print(f"⚠️  Unsupported OS: {system}")
        return None
    
    return cookies

def get_headers(post_id):
    """Generate headers for the request"""
    return {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "apollographql-client-name": "lite",
        "apollographql-client-version": "main-20260401-140543-04b3dba818",
        "content-type": "application/json",
        "graphql-operation": "useStatsPostNewChartDataQuery",
        "medium-frontend-app": "lite/main-20260401-140543-04b3dba818",
        "medium-frontend-path": f"/me/stats/post/{post_id}",
        "medium-frontend-route": "stats-post",
        "origin": "https://medium.com",
        "priority": "u=1, i",
        "referer": f"https://medium.com/me/stats/post/{post_id}",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    }

def get_graphql_payload(post_id):
    """Generate GraphQL payload for a specific post ID - Current month only"""
    now = datetime.now()
    
    # Start of current month (first day at midnight)
    start_of_month = datetime(now.year, now.month, 1, 0, 0, 0)
    
    # End of current month (today)
    end_of_month = now
    
    start_at = int(start_of_month.timestamp() * 1000)
    end_at = int(end_of_month.timestamp() * 1000)
    
    print(f"\n📅 Date Range:")
    print(f"   From: {start_of_month.strftime('%Y-%m-%d')}")
    print(f"   To:   {end_of_month.strftime('%Y-%m-%d')}")
    
    return [
        {
            "operationName": "useStatsPostNewChartDataQuery",
            "variables": {
                "postId": post_id,
                "startAt": start_at,
                "endAt": end_at,
                "postStatsDailyBundleInput": {
                    "postId": post_id,
                    "fromDayStartsAt": start_at,
                    "toDayStartsAt": end_at
                }
            },
            "query": """query useStatsPostNewChartDataQuery($postId: ID!, $startAt: Long!, $endAt: Long!, $postStatsDailyBundleInput: PostStatsDailyBundleInput!) {
  post(id: $postId) {
    id
    earnings {
      dailyEarnings(startAt: $startAt, endAt: $endAt) {
        ...newBucketTimestamps_dailyPostEarning
        __typename
      }
      __typename
    }
    publicationFeaturingEventsConnection(first: 25, after: "") {
      ... on PublicationFeaturingEventsConnection {
        edges {
          node {
            eventType
            occurredAt
            __typename
          }
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
  postStatsDailyBundle(postStatsDailyBundleInput: $postStatsDailyBundleInput) {
    buckets {
      ...newBucketTimestamps_postStatsDailyBundleBucket
      __typename
    }
    __typename
  }
}

fragment newBucketTimestamps_dailyPostEarning on DailyPostEarning {
  periodStartedAt
  amount
  __typename
}

fragment newBucketTimestamps_postStatsDailyBundleBucket on PostStatsDailyBundleBucket {
  dayStartsAt
  membershipType
  readersThatReadCount
  readersThatViewedCount
  readersThatClappedCount
  readersThatRepliedCount
  readersThatHighlightedCount
  readersThatInitiallyFollowedAuthorFromThisPostCount
  __typename
}"""
        }
    ]

def make_request(post_id, cookies):
    """Make the GraphQL request to Medium"""
    session = requests.Session()
    
    # Add cookies to session
    for name, value in cookies.items():
        session.cookies.set(name, value, domain=".medium.com", path="/")
    
    url = "https://medium.com/_/graphql"
    payload = get_graphql_payload(post_id)
    headers = get_headers(post_id)
    
    print(f"\n📡 Making request to: {url}")
    print(f"📝 Post ID: {post_id}")
    print(f"🍪 Cookies loaded: {list(cookies.keys())}")
    
    try:
        response = session.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

def display_current_month_stats(member_buckets, nonmember_buckets, post_id):
    """Display current month statistics with totals and latest day"""
    print("\n" + "="*70)
    print(f"📊 CURRENT MONTH STATISTICS")
    print(f"📝 Post ID: {post_id}")
    print(f"📅 Month: {datetime.now().strftime('%B %Y')}")
    print("="*70)
    
    if not member_buckets and not nonmember_buckets:
        print("⚠️  No data available for current month")
        return
    
    # Calculate totals for the month
    total_member_read = sum(b['readers_that_read'] for b in member_buckets)
    total_member_view = sum(b['readers_that_viewed'] for b in member_buckets)
    total_nonmember_read = sum(b['readers_that_read'] for b in nonmember_buckets)
    total_nonmember_view = sum(b['readers_that_viewed'] for b in nonmember_buckets)
    
    total_read = total_member_read + total_nonmember_read
    total_view = total_member_view + total_nonmember_view
    
    print(f"\n📈 MONTH TOTALS:")
    print("-"*70)
    print(f"\n👑 MEMBERS:")
    print(f"   📖 Total Reads:      {total_member_read}")
    print(f"   👁️  Total Views:      {total_member_view}")
    
    print(f"\n🌐 NON-MEMBERS:")
    print(f"   📖 Total Reads:      {total_nonmember_read}")
    print(f"   👁️  Total Views:      {total_nonmember_view}")
    
    print("\n" + "-"*70)
    print("📈 MONTH SUMMARY:")
    print(f"   Total Reads:        {total_read}")
    print(f"   Total Views:        {total_view}")
    
    if total_read > 0:
        print(f"   Member Read %:      {total_member_read / total_read * 100:.1f}%")
        print(f"   Non-member Read %:  {total_nonmember_read / total_read * 100:.1f}%")
    
    if total_view > 0:
        print(f"   Member View %:      {total_member_view / total_view * 100:.1f}%")
        print(f"   Non-member View %:  {total_nonmember_view / total_view * 100:.1f}%")
    
    # Get the most recent date
    all_dates = []
    for b in member_buckets:
        all_dates.append(b['date'])
    for b in nonmember_buckets:
        all_dates.append(b['date'])
    
    if all_dates:
        latest_date = max(all_dates)
        
        # Find latest day data
        latest_member = None
        latest_nonmember = None
        
        for b in member_buckets:
            if b['date'] == latest_date:
                latest_member = b
                break
        
        for b in nonmember_buckets:
            if b['date'] == latest_date:
                latest_nonmember = b
                break
        
        print("\n" + "="*70)
        print(f"📅 LATEST DAY: {latest_date}")
        print("="*70)
        
        if latest_member:
            print(f"\n👑 MEMBERS:")
            print(f"   📖 Reads:           {latest_member['readers_that_read']}")
            print(f"   👁️  Views:           {latest_member['readers_that_viewed']}")
            print(f"   👏 Claps:           {latest_member['readers_that_clapped']}")
            print(f"   💬 Replies:         {latest_member['readers_that_replied']}")
            print(f"   ✨ Highlights:      {latest_member['readers_that_highlighted']}")
            print(f"   👥 New followers:   {latest_member['new_followers']}")
        
        if latest_nonmember:
            print(f"\n🌐 NON-MEMBERS:")
            print(f"   📖 Reads:           {latest_nonmember['readers_that_read']}")
            print(f"   👁️  Views:           {latest_nonmember['readers_that_viewed']}")
            print(f"   👏 Claps:           {latest_nonmember['readers_that_clapped']}")
            print(f"   💬 Replies:         {latest_nonmember['readers_that_replied']}")
            print(f"   ✨ Highlights:      {latest_nonmember['readers_that_highlighted']}")
            print(f"   👥 New followers:   {latest_nonmember['new_followers']}")
        
        # Daily totals for latest day
        if latest_member and latest_nonmember:
            day_read = latest_member['readers_that_read'] + latest_nonmember['readers_that_read']
            day_view = latest_member['readers_that_viewed'] + latest_nonmember['readers_that_viewed']
            
            print("\n" + "-"*70)
            print("📈 DAY SUMMARY:")
            print(f"   Total Reads:        {day_read}")
            print(f"   Total Views:        {day_view}")
    
    # Show daily breakdown for the month
    if member_buckets or nonmember_buckets:
        print("\n" + "="*70)
        print("📅 DAILY BREAKDOWN (Current Month)")
        print("="*70)
        
        # Combine and sort by date
        all_days = {}
        for b in member_buckets:
            all_days[b['date']] = {'member': b, 'nonmember': None}
        for b in nonmember_buckets:
            if b['date'] in all_days:
                all_days[b['date']]['nonmember'] = b
            else:
                all_days[b['date']] = {'member': None, 'nonmember': b}
        
        for date in sorted(all_days.keys()):
            day_data = all_days[date]
            print(f"\n📅 {date}:")
            
            if day_data['member']:
                m = day_data['member']
                print(f"   👑 MEMBERS: Read: {m['readers_that_read']}, Views: {m['readers_that_viewed']}, Claps: {m['readers_that_clapped']}")
            
            if day_data['nonmember']:
                nm = day_data['nonmember']
                print(f"   🌐 NON-MEMBERS: Read: {nm['readers_that_read']}, Views: {nm['readers_that_viewed']}, Claps: {nm['readers_that_clapped']}")

def main():
    """Main function"""
    print("\n" + "="*70)
    print("🚀 MEDIUM POST STATISTICS FETCHER (Current Month)")
    print("="*70)
    
    # Try to get cookies from browser
    cookies = get_cookies_from_browser()
    
    if not cookies:
        print("\n❌ Could not find Medium cookies in browser")
        print("\nPlease make sure:")
        print("1. You're logged into Medium in your browser")
        print("2. Chrome/Firefox is closed (for cookie extraction)")
        print("3. You have visited Medium recently")
        sys.exit(1)
    
    # Check for required cookies
    if 'sid' not in cookies:
        print("\n❌ Missing 'sid' cookie - this is required for authentication")
        print("Please log out and log back into Medium, then close browser and try again")
        sys.exit(1)
    
    print(f"\n🍪 Found cookies: {list(cookies.keys())}")
    
    # Get post ID
    print("\n" + "="*70)
    print("📝 Enter Post ID")
    print("="*70)
    print("\nHow to find post ID:")
    print("  https://medium.com/@username/article-title-XXXXXXXXXXXX")
    print("  The post ID is the last part: XXXXXXXXXXXX")
    print()
    
    post_id = input("Post ID: ").strip()
    
    if not post_id:
        print("❌ No post ID provided. Exiting.")
        sys.exit(1)
    
    # Make the request
    response = make_request(post_id, cookies)
    
    if response:
        print(f"\n📡 Status Code: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("✅ Request successful!")
                
                # Debug: Show response structure
                print("\n🔍 DEBUG - Response Structure:")
                print(f"   Response type: {type(data)}")
                print(f"   Response length: {len(data) if isinstance(data, list) else 'N/A'}")
                
                if isinstance(data, list) and len(data) > 0:
                    print(f"   First item keys: {list(data[0].keys())}")
                    if 'data' in data[0]:
                        print(f"   Data keys: {list(data[0]['data'].keys())}")
                
                # Extract stats
                if isinstance(data, list) and len(data) > 0:
                    stats_data = data[0].get('data', {}).get('postStatsDailyBundle', {})
                    buckets = stats_data.get('buckets', [])
                    
                    print(f"\n🔍 DEBUG - Buckets found: {len(buckets)}")
                    
                    if buckets:
                        # Group buckets by date
                        member_buckets = []
                        nonmember_buckets = []
                        
                        for bucket in buckets:
                            date = datetime.fromtimestamp(bucket['dayStartsAt'] / 1000).strftime('%Y-%m-%d')
                            membership = bucket.get('membershipType', 'UNKNOWN')
                            
                            print(f"   {date} ({membership}): Read={bucket.get('readersThatReadCount', 0)}, Views={bucket.get('readersThatViewedCount', 0)}")
                            
                            bucket_data = {
                                'date': date,
                                'readers_that_read': bucket.get('readersThatReadCount', 0),
                                'readers_that_viewed': bucket.get('readersThatViewedCount', 0),
                                'readers_that_clapped': bucket.get('readersThatClappedCount', 0),
                                'readers_that_replied': bucket.get('readersThatRepliedCount', 0),
                                'readers_that_highlighted': bucket.get('readersThatHighlightedCount', 0),
                                'new_followers': bucket.get('readersThatInitiallyFollowedAuthorFromThisPostCount', 0)
                            }
                            
                            if membership == 'MEMBER':
                                member_buckets.append(bucket_data)
                            elif membership == 'NONMEMBER':
                                nonmember_buckets.append(bucket_data)
                        
                        # Display current month stats
                        if member_buckets or nonmember_buckets:
                            display_current_month_stats(member_buckets, nonmember_buckets, post_id)
                        else:
                            print("\n⚠️  No member/non-member data found for current month")
                    else:
                        print("\n⚠️  No buckets found in response")
                        print("\nFull response:")
                        print(json.dumps(data, indent=2))
                else:
                    print("\n⚠️  Unexpected response format")
                    print(json.dumps(data, indent=2))
                
            except json.JSONDecodeError as e:
                print(f"❌ Failed to parse JSON: {e}")
                print(f"Response text: {response.text[:500]}")
                
        elif response.status_code == 403:
            print("\n❌ ERROR: 403 Forbidden")
            print("Your cookies may be expired.")
            print("\nTo fix:")
            print("1. Log out of Medium in your browser")
            print("2. Log back in")
            print("3. Close your browser completely")
            print("4. Run this script again")
            
        else:
            print(f"\n❌ ERROR: {response.status_code}")
            print(f"Response: {response.text[:500]}")
    else:
        print("❌ Request failed")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)