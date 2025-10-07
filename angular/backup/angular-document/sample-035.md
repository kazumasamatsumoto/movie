# #035 「[src] 画像バインディング」

## 概要
`[src]`プロパティバインディングは、img要素のsrc属性を動的に設定する手法です。コンポーネントのプロパティ値に基づいて画像を動的に変更でき、ユーザーアクションや状態に応じた画像表示が可能になります。

## 学習目標
- [src]バインディングの基本構文を理解する
- 動的な画像パス管理の方法を学ぶ
- 画像の遅延読み込みやエラーハンドリングを実装できるようになる

## 技術ポイント
- `[src]`プロパティバインディング
- 動的な画像パス管理
- セキュリティ（URLサニタイゼーション）
- 画像読み込みエラーハンドリング

## 📺 画面表示用コード（動画用）

```typescript
// component.ts
export class ImageComponent {
  imageUrl = '/assets/images/profile.jpg';
}
```

```html
<!-- 画像バインディング -->
<img [src]="imageUrl" alt="プロフィール">
```

```html
<!-- エラーハンドリング -->
<img [src]="imageUrl"
     (error)="onImageError($event)"
     alt="画像">
```

## 💻 詳細実装例（学習用）

```typescript
// image-gallery.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-image-gallery',
  standalone: true,
  template: `
    <div class="gallery">
      <h2>画像ギャラリー</h2>

      <!-- 基本的な画像バインディング -->
      <img [src]="currentImage"
           [alt]="imageAlt"
           class="main-image">

      <!-- サムネイル一覧 -->
      <div class="thumbnails">
        @for (img of images; track img.id) {
          <img [src]="img.thumbnail"
               [alt]="img.title"
               [class.active]="currentImage === img.url"
               (click)="selectImage(img.url)"
               class="thumbnail">
        }
      </div>

      <!-- 動的パス生成 -->
      <div class="user-avatar">
        <img [src]="getUserAvatar(userId)"
             alt="ユーザーアバター">
      </div>

      <!-- エラーハンドリング -->
      <img [src]="remoteImage"
           (error)="handleImageError($event)"
           [src]="imageWithFallback"
           alt="リモート画像">

      <!-- 条件付き画像表示 -->
      <img [src]="user.hasAvatar ? user.avatarUrl : defaultAvatar"
           alt="プロフィール画像">

      <!-- Base64画像 -->
      <img [src]="base64Image" alt="Base64画像">
    </div>
  `,
  styles: [`
    .gallery {
      padding: 20px;
    }
    .main-image {
      width: 100%;
      max-width: 600px;
      height: auto;
      border-radius: 8px;
    }
    .thumbnails {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }
    .thumbnail {
      width: 100px;
      height: 100px;
      object-fit: cover;
      cursor: pointer;
      border: 2px solid transparent;
      border-radius: 4px;
    }
    .thumbnail.active {
      border-color: #007bff;
    }
    .thumbnail:hover {
      opacity: 0.8;
    }
  `]
})
export class ImageGalleryComponent {
  // 現在の画像
  currentImage = '/assets/images/photo1.jpg';
  imageAlt = '風景写真';

  // 画像一覧
  images = [
    { id: 1, url: '/assets/images/photo1.jpg', thumbnail: '/assets/thumbs/photo1.jpg', title: '風景1' },
    { id: 2, url: '/assets/images/photo2.jpg', thumbnail: '/assets/thumbs/photo2.jpg', title: '風景2' },
    { id: 3, url: '/assets/images/photo3.jpg', thumbnail: '/assets/thumbs/photo3.jpg', title: '風景3' }
  ];

  // ユーザー情報
  userId = 123;
  user = {
    hasAvatar: true,
    avatarUrl: '/assets/avatars/user123.jpg'
  };

  // フォールバック画像
  defaultAvatar = '/assets/images/default-avatar.png';
  remoteImage = 'https://example.com/image.jpg';
  imageWithFallback = this.remoteImage;

  // Base64画像例
  base64Image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...';

  selectImage(url: string) {
    this.currentImage = url;
  }

  getUserAvatar(userId: number): string {
    return `/assets/avatars/user${userId}.jpg`;
  }

  handleImageError(event: Event) {
    const img = event.target as HTMLImageElement;
    img.src = this.defaultAvatar;
    console.error('画像の読み込みに失敗しました');
  }

  onImageError(event: Event) {
    console.error('Image failed to load', event);
  }
}
```

### プロフィール画像の実装例

```typescript
// profile-picture.component.ts
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-profile-picture',
  standalone: true,
  template: `
    <div class="profile">
      <img [src]="profileImage()"
           [alt]="userName()"
           class="avatar"
           (error)="onLoadError()">

      <button (click)="changeImage()">画像変更</button>
    </div>
  `
})
export class ProfilePictureComponent {
  profileImage = signal('/assets/avatars/default.jpg');
  userName = signal('ユーザー名');

  changeImage() {
    const newImage = '/assets/avatars/new-avatar.jpg';
    this.profileImage.set(newImage);
  }

  onLoadError() {
    this.profileImage.set('/assets/avatars/default.jpg');
  }
}
```

## ベストプラクティス
- 画像パスは変数で管理し、ハードコーディングを避ける
- エラーハンドリングでフォールバック画像を設定する
- alt属性も動的にバインドして適切な代替テキストを提供する
- 大きな画像には遅延読み込み（loading="lazy"）を使用する
- 画像パスの生成ロジックはメソッドに分離する

## 注意点
- 外部URLを使用する場合はセキュリティに注意する
- 画像の存在チェックを行い、404エラーに対応する
- Base64画像は小さいアイコンなどに限定する（パフォーマンス）
- 画像のキャッシュ戦略を考慮する

## 関連技術
- [alt]バインディング
- (error)イベント
- DomSanitizer（外部URL用）
- NgOptimizedImage（v15+、パフォーマンス最適化）
- loading属性（遅延読み込み）
