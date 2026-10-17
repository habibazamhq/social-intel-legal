# Generates index/terms/privacy from one template (run: python3 build.py). Edit content here, not in the .html files.
HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Habib Social Intel</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&amp;family=Manrope:wght@400;600;700&amp;family=Sora:wght@600;700&amp;display=swap">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site">
  <a href="index.html" class="brand"><img src="logo.svg" alt="ha. Habib Azam" width="204" height="80"></a>
  <nav aria-label="Legal pages"><a href="terms.html"{t}>Terms</a><a href="privacy.html"{p}>Privacy</a></nav>
</header>
<main>
'''
FOOT = '''</main>
<footer class="site">
  <p>Habib Social Intel · operated by Habib Azam · <a href="mailto:habibazamhq@gmail.com">habibazamhq@gmail.com</a></p>
  <p class="mono">Not affiliated with or endorsed by TikTok.</p>
</footer>
</body>
</html>
'''
EFF = '<p class="meta mono">Effective date: 17 October 2026 · Last updated: 17 October 2026</p>'
CUR = ' aria-current="page"'

pages = {
'index.html': ('Legal', 'Terms of Service and Privacy Policy for Habib Social Intel, a private read-only TikTok analytics dashboard.', '', '', '''
<p class="eyebrow mono">Habib Social Intel</p>
<h1>Legal information<span class="dot">.</span></h1>
<p class="lead">Habib Social Intel is a private, read-only analytics dashboard that Habib Azam uses only for his own TikTok account, <strong>@habibazamhq</strong>. It reads profile statistics and video counts through the TikTok Display API. It never posts, comments, messages or likes, and it never sells or shares data.</p>
<div class="cards">
  <a class="card" href="terms.html"><span class="mono">01</span><h2>Terms of Service</h2><p>The rules for using the app.</p></a>
  <a class="card" href="privacy.html"><span class="mono">02</span><h2>Privacy Policy</h2><p>What data is read, how it is stored, and how to delete it.</p></a>
</div>
<p class="meta mono">Effective date: 17 October 2026</p>
'''),
'terms.html': ('Terms of Service', 'Terms of Service for Habib Social Intel.', CUR, '', f'''
<h1>Terms of Service<span class="dot">.</span></h1>
{EFF}
<p>These Terms govern use of <strong>Habib Social Intel</strong> (the "App"), a private analytics tool operated by Habib Azam ("we", "us"). By authorising the App with TikTok, you agree to these Terms and to our <a href="privacy.html">Privacy Policy</a>.</p>

<h2>1. What the App does</h2>
<p>The App is a private, read-only dashboard. It connects to TikTok through the official TikTok Display API using Login Kit with the scopes <code>user.info.basic</code>, <code>user.info.stats</code> and <code>video.list</code>. It displays profile statistics (such as follower and like counts) and counts for your public videos (views, likes, comments and shares) over time.</p>

<h2>2. Who may use it</h2>
<p>The App is intended solely for Habib Azam's own TikTok account (@habibazamhq). It is not offered to the public. You must be at least 18 years old, or the age of majority where you live, and you must be authorised to grant access to the TikTok account you connect.</p>

<h2>3. Read-only use</h2>
<p>The App only reads data. It does not and cannot post, upload, edit or delete content, comment, like, follow or send messages on your behalf, and it does not request any permissions that would allow this.</p>

<h2>4. Your responsibilities</h2>
<ul>
  <li>Keep your TikTok login secure. The App never asks for your TikTok password; sign-in happens on TikTok's own pages.</li>
  <li>Use the App in line with these Terms, TikTok's Terms of Service and Developer Terms, and applicable law.</li>
  <li>Do not attempt to misuse, reverse-engineer or overload the App or TikTok's services through it.</li>
</ul>

<h2>5. TikTok</h2>
<p>TikTok is a trademark of its owners. The App is an independent tool and is not affiliated with, sponsored by or endorsed by TikTok. TikTok's own terms and privacy policy apply to your use of TikTok.</p>

<h2>6. Revoking access</h2>
<p>You can disconnect the App at any time in the TikTok app under <em>Settings and privacy → Security → Apps and services permissions</em> (menu names may vary), or by emailing us. When access is revoked, the App stops collecting data. See the <a href="privacy.html">Privacy Policy</a> for deletion.</p>

<h2>7. No warranty</h2>
<p>The App is provided "as is" and "as available", without warranties of any kind. Metrics come from TikTok and may be delayed, incomplete or revised. They are for personal insight only and are not professional, financial or legal advice.</p>

<h2>8. Limitation of liability</h2>
<p>To the fullest extent permitted by applicable law, we are not liable for any indirect, incidental or consequential loss arising from use of the App. Nothing in these Terms limits liability that cannot be limited by law.</p>

<h2>9. Suspension and termination</h2>
<p>We may suspend or discontinue the App at any time. You may stop using it at any time by revoking access.</p>

<h2>10. Changes</h2>
<p>We may update these Terms. Changes are posted on this page with a new "Last updated" date. If you continue using the App after a change, you accept the updated Terms.</p>

<h2>11. Governing law</h2>
<p>These Terms are governed by the laws applicable in the place where the operator is established, without regard to conflict-of-law rules. This does not take away any mandatory consumer protections in your place of residence.</p>

<h2>12. Contact</h2>
<p>Questions about these Terms: <a href="mailto:habibazamhq@gmail.com">habibazamhq@gmail.com</a>.</p>
'''),
'privacy.html': ('Privacy Policy', 'Privacy Policy for Habib Social Intel: what TikTok data is read, how it is stored locally, and how to delete it.', '', CUR, f'''
<h1>Privacy Policy<span class="dot">.</span></h1>
{EFF}
<p class="lead">Short version: Habib Social Intel reads statistics for one TikTok account (@habibazamhq), stores them privately on the operator's own computer, and never sells or shares them. You can revoke access and ask for deletion at any time.</p>
<p>This Policy explains how <strong>Habib Social Intel</strong> (the "App"), operated by Habib Azam ("we", "us"), handles data obtained through the TikTok Display API.</p>

<h2>1. Data we collect</h2>
<p>Only after you approve access on TikTok's sign-in page, and only within these scopes:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Scope</th><th>Data read</th></tr></thead>
  <tbody>
    <tr><td><code>user.info.basic</code></td><td>Open ID, display name, avatar</td></tr>
    <tr><td><code>user.info.stats</code></td><td>Follower, following, likes and video counts</td></tr>
    <tr><td><code>video.list</code></td><td>Your public videos' IDs, titles, creation dates, links, and their view, like, comment and share counts</td></tr>
  </tbody>
</table></div>
<p>We also store the OAuth access and refresh tokens TikTok issues, so the App can refresh the data. We do <strong>not</strong> collect your password, messages, contacts, drafts, private videos, location, or the personal data of viewers or commenters. The App uses no cookies, analytics trackers or advertising on these pages or in the dashboard.</p>

<h2>2. How we use it</h2>
<p>Solely to show the account owner his own performance analytics: daily snapshots of the counts above, trends over time, and comparisons with his other social channels. We do not use the data for advertising, profiling, automated decisions about individuals, or training AI models.</p>

<h2>3. Storage and security</h2>
<p>Tokens and metrics are stored <strong>locally on a private machine</strong> controlled by the operator. Tokens sit in a restricted-permission file that is excluded from version control, and metrics are kept in a local database. Data is fetched over encrypted HTTPS connections directly from TikTok. Access is limited to the operator.</p>

<h2>4. Retention</h2>
<p>Metric snapshots are kept while the App is in use, so that trends can be shown. Tokens are kept only while access is authorised. When access is revoked or the App is discontinued, tokens are deleted, and stored metrics are deleted on request or when no longer needed.</p>

<h2>5. Sharing</h2>
<p><strong>None.</strong> We do not sell, rent, share or disclose TikTok data to any third party. The only exception is where disclosure is required by law, and then only to the extent required.</p>

<h2>6. Your rights and choices</h2>
<ul>
  <li><strong>Revoke access:</strong> in the TikTok app go to <em>Settings and privacy → Security → Apps and services permissions</em> (menu names may vary) and remove Habib Social Intel. Data collection stops immediately.</li>
  <li><strong>Access, correction or deletion:</strong> email <a href="mailto:habibazamhq@gmail.com">habibazamhq@gmail.com</a> and we will respond within 30 days. Deletion removes the stored tokens and all metrics for the account.</li>
  <li>Depending on where you live, you may have further rights under applicable data-protection law, such as the right to object or to complain to a supervisory authority.</li>
</ul>

<h2>7. Children</h2>
<p>The App is not directed at children and is used only by an adult account owner. We do not knowingly collect data from anyone under 18. Contact us if you believe we have, and we will delete it.</p>

<h2>8. International processing</h2>
<p>Data is processed on the operator's private machine, which may be in a different country from you. We apply the protections described in this Policy wherever the data is processed.</p>

<h2>9. Changes</h2>
<p>We may update this Policy. Changes are posted here with a new "Last updated" date. Material changes will not apply to previously collected data without your consent where the law requires it.</p>

<h2>10. Contact</h2>
<p>Habib Azam · <a href="mailto:habibazamhq@gmail.com">habibazamhq@gmail.com</a></p>
'''),
}
for f, (title, desc, t, p, body) in pages.items():
    open(f, 'w').write(HEAD.format(title=title, desc=desc, t=t, p=p) + body.strip() + '\n' + FOOT)
print('built', list(pages))
