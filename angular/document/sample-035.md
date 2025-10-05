# #035 「[src] 画像バインディング」台本

四国めたん「[src] 画像バインディングについて学びましょう！」
ずんだもん「画像のパスを動的に変更できるの？」
四国めたん「はい！プロパティバインディングで画像のsrc属性を動的に設定できます」
ずんだもん「どんな場面で使うの？」
四国めたん「ユーザーアバター、商品画像、条件に応じた画像切り替えなどです」
ずんだもん「エラー処理も必要？」
四国めたん「画像が読み込めない場合のフォールバック処理を追加しましょう」

---

## 📺 画面表示用コード

// 基本的な画像バインディング
```typescript
@Component({
  selector: 'app-image-binding',
  standalone: true,
  template: `
    <div class="image-demo">
      <h2>基本的な画像バインディング</h2>
      <img [src]="imageUrl" [alt]="imageAlt" width="200">
      <p>URL: {{imageUrl}}</p>
    </div>
  `,
  styles: [`
    .image-demo {
      padding: 20px;
      text-align: center;
    }
    img {
      border: 2px solid #007bff;
      border-radius: 8px;
    }
  `]
})
export class ImageBindingComponent {
  imageUrl = 'https://angular.io/assets/images/logos/angular/angular.svg';
  imageAlt = 'Angular Logo';
}
```

// 動的な画像切り替え
```typescript
@Component({
  selector: 'app-dynamic-image',
  standalone: true,
  template: `
    <div class="dynamic-demo">
      <h2>動的な画像切り替え</h2>
      <img [src]="currentImage" [alt]="currentAlt" width="150">
      <div class="controls">
        <button (click)="changeImage('logo')">ロゴ</button>
        <button (click)="changeImage('icon')">アイコン</button>
      </div>
    </div>
  `,
  styles: [`
    .dynamic-demo {
      padding: 20px;
      text-align: center;
    }
    .controls button {
      margin: 5px;
      padding: 8px 16px;
    }
  `]
})
export class DynamicImageComponent {
  currentImage = '';
  currentAlt = '';
  
  images = {
    logo: 'https://angular.io/assets/images/logos/angular/angular.svg',
    icon: 'https://angular.io/assets/images/logos/angular/angular.png'
  };
  
  changeImage(type: string) {
    this.currentImage = this.images[type as keyof typeof this.images];
    this.currentAlt = `${type} image`;
  }
}
```

// エラーハンドリング付き画像
```typescript
@Component({
  selector: 'app-error-handling',
  standalone: true,
  template: `
    <div class="error-demo">
      <h2>エラーハンドリング付き画像</h2>
      <img [src]="imageUrl" 
           [alt]="imageAlt"
           (error)="onImageError()"
           (load)="onImageLoad()"
           width="200">
      <p>{{statusMessage}}</p>
    </div>
  `,
  styles: [`
    .error-demo {
      padding: 20px;
      text-align: center;
    }
  `]
})
export class ErrorHandlingComponent {
  imageUrl = 'https://invalid-url.com/image.jpg';
  imageAlt = '画像';
  statusMessage = '読み込み中...';
  
  onImageError() {
    this.statusMessage = '画像の読み込みに失敗しました';
    this.imageUrl = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPuaXoOazleiDveWKoOi9vTwvdGV4dD48L3N2Zz4=';
  }
  
  onImageLoad() {
    this.statusMessage = '画像の読み込み完了';
  }
}
```
