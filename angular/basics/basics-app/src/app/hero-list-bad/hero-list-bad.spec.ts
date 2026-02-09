import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeroListBad } from './hero-list-bad';

describe('HeroListBad', () => {
  let component: HeroListBad;
  let fixture: ComponentFixture<HeroListBad>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HeroListBad]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HeroListBad);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
