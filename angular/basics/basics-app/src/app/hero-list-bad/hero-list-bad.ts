import { Component, inject, signal } from '@angular/core';
import { HeroService, Hero } from '../hero.service';

@Component({
  selector: 'app-hero-list-bad',
  imports: [],
  templateUrl: './hero-list-bad.html',
  styleUrl: './hero-list-bad.scss',
})
export class HeroListBad {
  private readonly heroService = inject(HeroService);

  heroes = signal<Hero[]>([]);

  constructor() {
    // ❌ 悪い例：constructorでAPI呼び出し
    // 問題点：
    // - @Inputがまだ設定されていない
    // - コンポーネントの状態が不完全
    // - Angularのライフサイクル管理外
    this.heroService.getHeroes()
      .subscribe(data => {
        this.heroes.set(data);
      });
    // さらに問題：
    // - loading状態の管理がない
    // - 購読解除されないのでメモリリーク
    // - エラーハンドリングがない
  }
}
