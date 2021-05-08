'''
5. Anda adalah seorang software developer di sebuah startup website blog bernama
PT Blogg. Suatu hari anda diberi tugas untuk memperbaiki sebuah code yang
berfungsi untuk menghitung total likes dari sebuah blog. Ini adalah codenya :

Code diatas masih menimbulkan KeyError karena ada beberapa post berbentuk
dictionary yang tidak memiliki key “Likes”, buatlah sebuah exception KeyError yang
akan membuat key baru bernama “Likes” dengan value 0 dan print message “Post ini
tidak memiliki likes”. (Note: Copy P)
'''

blog_posts = [
{'Photos': 3, 'Likes': 21, 'Comments': 2},
{'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5,
'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4,
'Shares': 2}
]
total_likes = 0
postn = 1
for post in blog_posts:
    print("Post ke - ",postn)
    postn+=1
    #Tambahkan code disini
    try:
        jlh = post['Likes']
        print("Post Ini Memiliki",jlh,"Likes")
    except KeyError:
        print("Post Ini Tidak Memiliki Likes")
    else:
        total_likes = total_likes + post['Likes']
print("Jumlah Total Likes Adalah ", total_likes)