# #130 「Component 通信の実践例」

## 概要
複数の通信手段（@Input/@Output、共有サービス、Signal）を組み合わせた実践的なコンポーネント構成例を紹介します。

## 学習目標
- 親子通信とサービス共有を併用したアーキテクチャを理解する
- SignalInput/SignalOutputでStatefulなコンポーネントを構築する方法を習得する
- UIと状態管理の境界を整理し、拡張しやすい構成を学ぶ

## 技術ポイント
- **親子連携**: 親がフォーム設定を渡し、子がイベントで結果を通知
- **共有サービス**: サービスが結果をキャッシュ/共有
- **Signal API**: SignalInput/SignalOutputでリアクティブにデータを扱う

```typescript
readonly formConfig = signal({ theme: 'dark', notify: true });
```

```html
<app-settings-panel
  [config]="formConfig()"
  (configChange)="formConfig.set($event)"
></app-settings-panel>
```

```typescript
service.save(formConfig()).then(() => toast.open());
```

## 💻 詳細実装例（学習用）
```typescript
// settings-store.service.ts
import { Injectable, signal } from '@angular/core';

export type Settings = { theme: 'light' | 'dark'; notify: boolean };

@Injectable({ providedIn: 'root' })
export class SettingsStore {
  readonly settings = signal<Settings>({ theme: 'light', notify: true });

  update(settings: Settings): void {
    this.settings.set(settings);
  }
}
```

```typescript
// settings-panel.component.ts
import { Component, computed, effect, input, output } from '@angular/core';
import { Settings } from './settings-store.service';

@Component({
  selector: 'app-settings-panel',
  standalone: true,
  templateUrl: './settings-panel.component.html',
})
export class SettingsPanelComponent {
  readonly config = input<Settings>({ required: true });
  readonly configChange = output<Settings>();

  readonly themeLabel = computed(() =>
    this.config().theme === 'dark' ? 'ダーク' : 'ライト',
  );

  toggleTheme(): void {
    const next: Settings = {
      ...this.config(),
      theme: this.config().theme === 'dark' ? 'light' : 'dark',
    };
    this.configChange.emit(next);
  }

  toggleNotify(): void {
    this.configChange.emit({ ...this.config(), notify: !this.config().notify });
  }
}
```

```html
<!-- settings-panel.component.html -->
<section>
  <h3>テーマ: {{ themeLabel() }}</h3>
  <button type="button" (click)="toggleTheme()">テーマ切替</button>

  <h3>通知: {{ config().notify ? 'ON' : 'OFF' }}</h3>
  <button type="button" (click)="toggleNotify()">通知切替</button>
</section>
```

```typescript
// settings-page.component.ts
import { Component, DestroyRef, effect, inject, signal } from '@angular/core';
import { Settings, SettingsStore } from './settings-store.service';
import { SettingsPanelComponent } from './settings-panel.component';

@Component({
  selector: 'app-settings-page',
  standalone: true,
  imports: [SettingsPanelComponent],
  templateUrl: './settings-page.component.html',
})
export class SettingsPageComponent {
  private readonly store = inject(SettingsStore);
  readonly config = signal<Settings>(this.store.settings());

  constructor(destroyRef: DestroyRef) {
    effect(
      () => {
        console.log('Store settings changed', this.store.settings());
      },
      { scope: destroyRef },
    );
  }

  save(): void {
    this.store.update(this.config());
  }
}
```

```html
<!-- settings-page.component.html -->
<app-settings-panel
  [config]="config()"
  (configChange)="config.set($event)"
></app-settings-panel>
<button type="button" (click)="save()">保存</button>
<p>現在の共有設定: {{ config() | json }}</p>
```

## ベストプラクティス
- UIコンポーネント（SettingsPanelComponent）はSignalInput/SignalOutputでViewの責務に集中させる
- 親コンポーネントでSignalを保持し、共有サービスへ保存することで状態管理を一元化する
- effectを利用して変更を監視し、ロギングやサイドエフェクトを実装する

## 注意点
- SignalInput/SignalOutputを使う際はAngularバージョンとAPI安定度を確認する
- 状態が複雑になる場合は状態管理ライブラリへの移行を検討する
- 保存処理はtry/catchやエラーハンドリングを追加し、ユーザーへのフィードバックを忘れない

## 関連技術
- Angular Signals + Inject API
- 共有サービスとState Storeパターン
- UI/State分離（Smart & Presentational Components）
